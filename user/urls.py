from django.urls import path
from .views import CandidateAPIView

urlpatterns = [
    path('candidate/<int:pk>', CandidateAPIView.as_view(), name='candidate_modify'),
    path('candidate/', CandidateAPIView.as_view(), name='candidate_create'),
    path('employee/', CandidateAPIView.as_view(), name='crud_employee'),
    path('department/', CandidateAPIView.as_view(), name='crud_department'),
]
