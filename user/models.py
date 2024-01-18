import uuid

from django.contrib.postgres.fields import ArrayField

from test_app.models import Test


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    head = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="head_of_department")
    requirements = ArrayField(models.CharField(max_length=100), size=50)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    department = models.ForeignKey("Department", null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="employee_department")
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Candidate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resume')
    skill_set = ArrayField(models.CharField(max_length=100))
    score = models.DecimalField(max_digits=5, decimal_places=2)
    alloted_test = models.ForeignKey(Test, on_delete=models.SET_NULL, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class CustomUserManager(BaseUserManager):
    use_in_migrations = True


class User(AbstractUser):
    password = models.CharField(max_length=128)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, blank=True, null=True)
