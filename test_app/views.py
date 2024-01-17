from rest_framework.views import APIView
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from test_app.models import Test, Question, TestResponse
from test_app.serializers import TestSerializer, QuestionSerializer, TestResponseSerializer
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger(name="django")
class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "created_by", "assigned_to", "status"]

    def post(self, request, *args, **kwargs):
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

    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            question_id = request.data.get("id")
            question = Question.objects.get(pk=question_id)
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
        test_id = kwargs.get('pk')
        test = TestResponse.objects.get(pk=test_id)
        serializer = TestSerializer(test, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
