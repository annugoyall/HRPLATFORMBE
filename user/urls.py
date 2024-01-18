from django.urls import path
from .views import CandidateAPIView, EmployeeAPIView, DepartmentAPIView

urlpatterns = [
    path('candidate/<int:pk>', CandidateAPIView.as_view(), name='candidate_modify'),
    path('candidate/', CandidateAPIView.as_view(), name='candidate_create'),
    path('employee/<int:pk>', EmployeeAPIView.as_view(), name='employee_modify'),
    path('employee/', EmployeeAPIView.as_view(), name='employee_create'),
    path('department/<int:pk>', DepartmentAPIView.as_view(), name='department_modify'),
    path('department/', DepartmentAPIView.as_view(), name='department_create'),
]
