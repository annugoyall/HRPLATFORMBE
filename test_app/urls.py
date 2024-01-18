from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet, QuestionViewSet, TestResponseViewSet

router = DefaultRouter()
router.register(r'test', TestViewSet, basename='TestView')
router.register(r'question', QuestionViewSet, basename='TestView')
router.register(r'test_response', TestResponseViewSet, basename='TestView')


urlpatterns = [
    path('', include(router.urls)),
]