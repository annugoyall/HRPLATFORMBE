# views.py

from uuid import UUID

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Candidate, Department, Employee
from .serializers import CandidateSerializer, DepartmentSerializer, EmployeeSerializer


class CandidateAPIView(ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        candidate = self.get_object(pk)
        if not candidate:
            return Response(data={"Message":"Candidate not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        candidate_obj = self.get_object(pk)
        if candidate_obj:
            candidate_obj.delete()
            return Response(data={"MESSAGE": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={"MESSAGE": "Candidate not found"}, status=status.HTTP_204_NO_CONTENT)



class DepartmentAPIView(ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        pk = request.GET.get('id')
        department = self.get_object(pk)
        if not department:
            return Response(data={"Message":"Department not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        department_obj = self.get_object(pk)
        if not department_obj:
            return Response(data={"Message":"Department not found"},status=status.HTTP_404_NOT_FOUND)
        department_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeAPIView(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"Message":str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, *args, **kwargs):
        employee_id = kwargs.get('pk')
        employee = self.get_object(employee_id)
        if not employee:
            return Response(data={"Message":"Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        employee_obj = self.get_object(pk)
        if not employee_obj:
            return Response(data={"Message":"Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        employee_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
