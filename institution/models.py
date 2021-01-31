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


    class Level(models.TextChoices):
        PRE_KINDERGARDEN = 'PREK'
        KINDERGARDEN     = 'KIND'
        GRADE            = 'GRAD'
        UNDER_GARDUATE   = 'UNGR'
        GARDUATE         = 'PGRA'
        POST_GARDUATE    = 'POST'
        VOCATIONAL       = 'VOCA'
        TECHNICAL        = 'TECH'



    class Status(models.TextChoices):
        FRESHMAN        = 'FR'
        SOPHOMORE       = 'SO'
        JUNIOR          = 'JU'
        SENIOR          = 'SE'


    class Category(models.TextChoices):
        PRIMARY_EDUCATION       = 'PS'
        SECONDARY_EDUCATION     = 'SS'
        POSTSECONDARY_EDUCATION = 'PE'
        VOCATIONAL_EDUCATION    = 'VS'
        TECHNICAL_EDUCATION     = 'TS'

    id       = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title    = models.CharField(max_length=50)
    category = models.CharField(max_length=2, choices=Category.choices,
                                 blank=True, null=True)
    level    = models.CharField(max_length=4, choices=Level.choices)
    grade    = models.CharField(max_length=6)
    ages     = models.CharField(max_length=6)
    duration = models.CharField(max_length=6)

    def __str__(self):
        return self.title


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    achievement = models.CharField(max_length=25)
    duration = models.CharField(max_length=6)
    description = models.TextField()
    map         = models.ManyToManyField(ISCEDLevel, through='ProgramMap')

    def __str__(self):
        return self.name


class ProgramMap(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    step    = models.PositiveIntegerField()
    path    = models.OneToOneField(ISCEDLevel, on_delete=models.CASCADE)
