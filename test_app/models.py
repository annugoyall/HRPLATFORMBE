from django.contrib.postgres.fields import ArrayField
from django.db import models
from .constants import TEST_STATUS_CHOICES, QUESTION_TYPE_CHOICES
from django.contrib.postgres.fields import ArrayField

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    question_type = models.CharField(choices=QUESTION_TYPE_CHOICES, max_length=10, default="MCQ")
    tags = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    correct_answer = models.TextField()
    other_dependencies = models.JSONField(blank=True, null=True)

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    questions = models.ManyToManyField(Question, blank=True, related_name="tests")
    status = models.CharField(choices=TEST_STATUS_CHOICES, max_length=10, default="Pending")
    conduced_on = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("user.Employee", blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="created_by")
    assigned_to = models.ForeignKey("user.Department", blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name="assigned_to")
    def __str__(self):
            return self.name
class TestResponse(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey("user.Candidate", blank=True, null=True, on_delete=models.SET_NULL)
    test = models.ForeignKey(Test, null=True, blank=True, on_delete=models.SET_NULL)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.SET_NULL)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
