# serializers.py

from rest_framework import serializers
from .models import Candidate, Department, Employee, User


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeGetSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    department = serializers.CharField()
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    requirements = serializers.ListField(allow_null=True, allow_empty=True)
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentGetSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    head = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    requirements = serializers.ListField(allow_null=True, allow_empty=True)
    class Meta:
        model = Department
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    resume = serializers.FileField(required=False)
    skill_set = serializers.ListField(required=False)
    score = serializers.CharField(required=False)

    class Meta:
        model = Candidate
        fields = '__all__'

class CandidateGetSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    resume = serializers.FileField(required=False)
    skill_set = serializers.ListField(required=False)
    score = serializers.CharField(required=False)
    alloted_test = serializers.CharField(required=False)

    class Meta:
        model = Candidate
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
