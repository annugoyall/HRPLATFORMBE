from django.contrib import admin
from django.urls import path, include
from .views import parse_resume_view

urlpatterns = [
    path('parse_resume/<int:candidate_id>/', parse_resume_view, name='parse_resume'),
]