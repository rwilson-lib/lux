from django.db import models
import uuid


from instructor.models import Instructor
from personal.models import (Address, Contact, Personal, Document)
from student.models import Student


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    addresses = models.ManyToManyField(Address, through='InstitutionAddress')
    contacts = models.ManyToManyField(Contact, through='InstitutionContact')
    documents = models.ManyToManyField(Document, through='InstitutionDocument')

    def __str__(self):
        return self.name

class InstitutionAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class InstitutionContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE)


class InstitutionDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class ISCEDLevel(models.Model):
    level =  models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    year = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
