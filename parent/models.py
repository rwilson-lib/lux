from django.db import models
import uuid

# Create your models here.

from personal.models import Personal
from student.models import Student

class Parent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='StudentParent')

    def __str__(self):
        return self.personal.__str__()

class StudentParent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    # school

    class Meta:
        unique_together = ('student', 'parent')
