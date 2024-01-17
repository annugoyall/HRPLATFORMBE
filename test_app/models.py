from django.contrib.postgres.fields import ArrayField
from django.db import models

from .constants import TEST_STATUS_CHOICES, QUESTION_TYPE_CHOICES


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    question_type = models.CharField(choices=QUESTION_TYPE_CHOICES, max_length=50, default="MCQ")
    tags = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    correct_answer = models.TextField()
    other_dependencies = models.JSONField(blank=True, null=True)


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question)
    status = models.CharField(choices=TEST_STATUS_CHOICES, max_length=10, default="Pending")
    conduced_on = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("user.Employee", blank=True, null=True, on_delete=models.SET_NULL)
    alloted_to = models.ManyToManyField("user.Candidate")


class TestResponse(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey("user.Candidate", blank=True, null=True, on_delete=models.SET_NULL)
    test = models.ForeignKey("Test", blank=True, null=True, on_delete=models.SET_NULL)
    question = models.ForeignKey("Question", blank=True, null=True, on_delete=models.SET_NULL)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
