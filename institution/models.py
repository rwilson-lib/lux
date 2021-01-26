''''
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import uuid


from instructor.models import Instructor
from personal.models import Address, Personal
from student.models import Student


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class ISCEDLevel(models.Model):
    level =  models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    year = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class AcademicYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    semester = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level = models.ManyToManyField(ISCEDLevel)
    course = models.CharField(max_length=100)
    code = models.PositiveIntegerField(blank=True, null=True)
    credit_hour = models.PositiveIntegerField(default=1)
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return "{} {} {}hr".format(self.course, self.code, self.credit_hour)



class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    motto = models.CharField(max_length=25)
    mascot = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    levels = models.ManyToManyField(ISCEDLevel)
    year_founded = models.DateField()

    def __str__(self):
        return "{} -:- {}".format(self.institution.name, self.name)


class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Campus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, default="")
    elevation =  models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    floor = models.PositiveIntegerField(blank=True, null=True)
    dimension = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return "{}-[{}] floor: {} name: {}".format(
            self.building.name,
            self.building.elevation,
            self.floor,
            self.name
        )

    def clean(self):
        errors = {}
        if self.floor > self.building.elevation:
            errors['floor'] = _(
                "exceeded building elevation value between 0 - {}"
                .format(self.building.elevation))
        if errors:
            raise ValidationError(
                errors
            )


class Enroll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_id = models.CharField(max_length=25, unique=True)
    year = models.DateField()
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)


    def __str__(self):
        return self.school_id


class Postion(models.Model):
    postion = models.CharField(max_length=25)
    description = models.TextField()


class Staff():
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    postions =  models.ManyToManyField(Postion)
'''
