from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from test_app.models import Test, Question, TestResponse
from test_app.serializers import TestSerializer, QuestionSerializer, TestResponseSerializer


class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

    def patch(self, request, *args, **kwargs):
        test_id = kwargs.get('pk')
        test = Test.objects.get(pk=test_id)
        serializer = TestSerializer(test, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

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
