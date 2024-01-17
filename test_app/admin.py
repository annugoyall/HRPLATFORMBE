from django.contrib import admin

# Register your models here.
from test_app.models import Test, Question, TestResponse
from user.models import Candidate, Department, Employee
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(TestResponse)
admin.site.register(Candidate)
admin.site.register(Department)
admin.site.register(Employee)