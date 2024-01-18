# views.py
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse,StreamingHttpResponse

from test_app.models import Test
from .models import Candidate, Department, Employee, User
from .serializers import CandidateSerializer, DepartmentSerializer, EmployeeSerializer, UserSerializer
from .models import Candidate, Department, Employee
from .serializers import CandidateSerializer, DepartmentSerializer, EmployeeSerializer, EmployeeGetSerializer, DepartmentGetSerializer, CandidateGetSerializer


class CandidateAPIView(ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CandidateGetSerializer

    def create(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        candidate_id = kwargs.get("pk")
        candidate = Candidate.objects.get(id=int(candidate_id))
        if not candidate:
            return Response(data={"Message": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CandidateSerializer(candidate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     candidate_obj = self.get_object(pk)
    #     if candidate_obj:
    #         candidate_obj.delete()
    #         return Response(data={"MESSAGE": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response(data={"MESSAGE": "Candidate not found"}, status=status.HTTP_204_NO_CONTENT)


class DepartmentAPIView(ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DepartmentGetSerializer

    def create(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        department_id = kwargs.get("pk")
        if not department_id:
            return Response(data={"Message": "Department id is required"}, status=status.HTTP_404_NOT_FOUND)
        department = Department.objects.get(id=department_id)
        if not department:
            return Response(data={"Message": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        head_id = request.data.get("head")
        if head_id:
            head = Employee.objects.get(id=head_id).id
            request.data["head"] = head
        serializer = DepartmentSerializer(department, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     department_obj = self.get_object(pk)
    #     if not department_obj:
    #         return Response(data={"Message": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
    #     department_obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeAPIView(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeGetSerializer

    def create(self, request, *args, **kwargs):
        try:
            department_id = request.data.get("department")
            if not department_id:
                return Response(data={"Message": "Department id is required"}, status=status.HTTP_404_NOT_FOUND)
            # request.data["department"] = Department.objects.get(id=int(department_id)).id
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"Message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        employee_id = kwargs.get("pk")
        if not employee_id:
            return Response(data={"Message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        employee = Employee.objects.get(id=int(employee_id))
        department_id = request.data.get("department")
        if department_id:
            request.data["department"] = Department.objects.get(id=int(department_id)).id
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     employee_obj = self.get_object(pk)
    #     if not employee_obj:
    #         return Response(data={"Message":"Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    #     employee_obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        resp_data = serializer.data
        candidate_name = resp_data['first_name']+resp_data['last_name']
        candidate_obj = Candidate.objects.create(name=candidate_name)
        candidate_obj.save()
        user_obj = User.objects.get(id=resp_data['id'])
        user_obj.candidate = candidate_obj
        user_obj.save()
        resp_data['candidate'] = candidate_obj.id
        return Response(resp_data, status=status.HTTP_201_CREATED, headers=headers)
