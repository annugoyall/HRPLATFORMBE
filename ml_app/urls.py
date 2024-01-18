from django.contrib import admin
from django.urls import path, include
from .views import ParseResumeView

urlpatterns = [
    path('parse_resume/', ParseResumeView.as_view(), name='parse_resume'),
]