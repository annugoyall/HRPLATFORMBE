from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet, QuestionViewSet, TestResponseViewSet, GetCandidateTestResponseView

router = DefaultRouter()
router.register(r'test', TestViewSet, basename='TestView')
router.register(r'question', QuestionViewSet, basename='TestView')
router.register(r'test_response', TestResponseViewSet, basename='TestView')


urlpatterns = [
    path('get_candidate_test_response/<id>', GetCandidateTestResponseView.as_view(), name='get_candidate_test_response'),
    path('', include(router.urls)),
]