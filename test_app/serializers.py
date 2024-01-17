# serializers.py

from rest_framework import serializers
from .models import Test, Question, TestResponse

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class TestResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResponse
        fields = '__all__'