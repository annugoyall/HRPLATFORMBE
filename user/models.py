import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
# Department, Employee, Candidate
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    head = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    requirements = ArrayField(models.CharField(max_length=100),size=50)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    id = models.AutoField()
    resume = models.FileField()