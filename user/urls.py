from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateAPIView, EmployeeAPIView, DepartmentAPIView, UserAPIView, get_resume_by_id

router = DefaultRouter()
router.register(r'candidate', CandidateAPIView, basename='CandidateAPIView')
router.register(r'employee', EmployeeAPIView, basename='EmployeeAPIView')
router.register(r'department', DepartmentAPIView, basename='DepartmentAPIView')
router.register(r'user', UserAPIView, basename='UserAPIView')

urlpatterns = [
    path('', include(router.urls)),
    path('get_file/<str:candidate_id>/', get_resume_by_id, name='get_resume_by_id'),
]
