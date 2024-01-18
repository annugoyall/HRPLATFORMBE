# serializers.py
import json

from rest_framework import serializers
from .models import Test, Question, TestResponse


class TestSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    conduced_on = serializers.CharField(required=False)
    created_at = serializers.CharField(required=False)
    modified_at = serializers.CharField(required=False)
    created_by = serializers.CharField(required=False)
    assigned_to = serializers.CharField(required=False)

    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    created_at = serializers.CharField(required=False)

    class Meta:
        model = Question
        fields = '__all__'


class TestResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestResponse
        fields = '__all__'
