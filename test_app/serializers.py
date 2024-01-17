# serializers.py
import json

from rest_framework import serializers
from .models import Test, Question, TestResponse


class TestSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    created_at = serializers.CharField()

    class Meta:
        model = Test
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    conduced_on = serializers.CharField()
    created_at = serializers.CharField()
    modified_at = serializers.CharField()
    created_by = serializers.CharField()
    assigned_to = serializers.CharField()

    class Meta:
        model = Question
        fields = '__all__'


class TestResponseSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    candidate = serializers.CharField()
    test = serializers.CharField()
    question = serializers.CharField()
    created_at = serializers.CharField()

    class Meta:
        model = TestResponse
        fields = '__all__'
