from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from test_app.models import Test, Question, TestResponse
from user.models import Candidate, Department, Employee
from test_app.serializers import TestSerializer, QuestionSerializer, TestResponseSerializer, TestGetSerializer
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger(name="django")


class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "created_by", "assigned_to", "status"]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TestGetSerializer

    @action(detail=False, methods=["GET"], url_path="get-test-by-id", url_name="get-test-by-id")
    def get_test_by_id(self, request, *args, **kwargs):
        try:
            test_id = request.query_params.get("id")
            if test_id:
                test = Test.objects.get(id=test_id)
                question_ids = list(test.questions.all())
                question_ids = [question.id for question in question_ids]
                test_serializer = TestGetSerializer(test)
                questions = Question.objects.filter(id__in=question_ids)
                question_serializer = QuestionSerializer(questions, many=True)
                response = test_serializer.data
                response["questions"] = question_serializer.data
                return Response(response)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        try:
            serializer = TestSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            test_id = request.data.get("id")
            test = Test.objects.get(id=test_id)
            questions = request.data.get("questions")
            if test is not None:
                if questions:
                    existing_questions = list(test.questions.all())
                    existing_questions = [question.id for question in existing_questions]
                    combined_questions = existing_questions + questions
                    request.data["questions"] = combined_questions
                if request.data.get("assigned_to"):
                    assigned_to_id = request.data.get("assigned_to")
                    request.data["assigned_to"] = Department.objects.get(id=int(assigned_to_id)).id
                if request.data.get("created_at"):
                    created_at_id = request.data.get("created_at")
                    request.data["created_at"] = Employee.objects.get(id=int(created_at_id)).id
                serializer = TestSerializer(test, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["question_type"]

    def create(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            question_id = request.data.get("id")
            question = Question.objects.get(pk=int(question_id))
            serializer = QuestionSerializer(question, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            question_id = request.data.get("id")
            question = Question.objects.get(pk=question_id)
            question.delete()
            return Response("Question deleted successfully", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class TestResponseViewSet(ModelViewSet):
    serializer_class = TestResponseSerializer
    queryset = TestResponse.objects.all()

    def patch(self, request, *args, **kwargs):
        try:
            candidate = request.data.get("candidate")
            questions = request.data.get("question")
            correct_answers = 0
            for question in questions:
                question_id = question.get("id")
                answer = question.get("selectedOptionKey")
                request.data["answer"] = answer
                request.data["question"] = int(question_id)
                serializer = TestResponseSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                if Question.objects.get(pk=question_id).correct_answer == answer:
                    correct_answers += 1
            score = (correct_answers / len(questions)) * 100
            candidate = Candidate.objects.get(id=int(candidate))
            candidate.score = score
            candidate.save()
            return Response("Test submitted successfully", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
