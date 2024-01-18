# serializers.py

from rest_framework import serializers
from .models import Candidate, Department, Employee, User


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    department = serializers.CharField(required=False)
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    head = serializers.CharField(allow_blank=True, allow_null=True)
    requirements = serializers.ListField(allow_null=True,allow_empty=True)
    class Meta:
        model = Department
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    resume = serializers.FileField()
    skill_set = serializers.ListField()
    score = serializers.CharField()

    class Meta:
        model = Candidate
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
