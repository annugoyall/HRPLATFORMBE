# views.py

from uuid import UUID

from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from .models import Candidate, Department, Employee
from .serializers import CandidateSerializer, DepartmentSerializer, EmployeeSerializer


class CandidateAPIView(APIView):
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('id')
        candidate = self.get_object(pk)
        if not candidate:
            return JsonResponse(data={"Message":"Candidate not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('id')
        candidate_obj = self.get_object(pk)
        if candidate_obj:
            candidate_obj.delete()
            return JsonResponse(data={"MESSAGE": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse(data={"MESSAGE": "Candidate not found"}, status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        id = UUID(pk)
        try:
            return Candidate.objects.get(id=id)
        except Exception as e:
            return None


class DepartmentAPIView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('id')
        department = self.get_object(pk)
        if not department:
            return JsonResponse(data={"Message":"Department not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('id')
        department_obj = self.get_object(pk)
        if not department_obj:
            return JsonResponse(data={"Message":"Department not found"},status=status.HTTP_404_NOT_FOUND)
        department_obj.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        id = UUID(pk)
        try:
            return Department.objects.get(id=id)
        except Department.DoesNotExist:
            return None



class EmployeeAPIView(APIView):
    def get(self, request):
        all_employee = Employee.objects.all()
        serializer = EmployeeSerializer(all_employee, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.GET.get('id')
        employee = self.get_object(pk)
        if not employee:
            return JsonResponse(data={"Message":"Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.GET.get('id')
        employee_obj = self.get_object(pk)
        if not employee_obj:
            return JsonResponse(data={"Message":"Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        employee_obj.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise JsonResponse(status=status.HTTP_404_NOT_FOUND)
