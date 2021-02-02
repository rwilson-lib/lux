from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid


# from academic.models import AcademicYear

from institution.models import Institution, ISCEDLevel
from instructor.models import Instructor
from personal.models import Personal
from student.models import Student


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    motto = models.CharField(max_length=25)
    mascot = models.ImageField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    divisions = models.ManyToManyField(ISCEDLevel)
    year_founded = models.DateField()

    def __str__(self):
        return "{} -:- {}".format(self.institution.name, self.name)



class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level = models.ManyToManyField(ISCEDLevel)
    title = models.CharField(max_length=100)
    code  = models.PositiveIntegerField(blank=True, null=True)
    credit_hour = models.PositiveIntegerField(default=1)
    instructors = models.ManyToManyField(Instructor, through='CourseInstructor')

    def __str__(self):
        return "{} {} {}hr".format(self.title, self.code, self.credit_hour)


class CourseInstructor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)


class SchoolCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    courses = models.ManyToManyField(Course, through='CollegeCourse')

    def __str__(self):
        return self.name


class CollegeCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Enroll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=25, unique=True)
    # academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)


    def __str__(self):
        return "{} {}".format(self.id_number, self.student)


class Position(models.Model):
    position = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.position


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_id = models.CharField(max_length=25,unique=True)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)
    positions    = models.ManyToManyField(Position)
    hired_date  = models.DateField()
    fully_time  = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.personal)


class StudentStatus(models.Model):
    class YearInSchool(models.TextChoices):
        FRESHMAN  = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR    = 'JR', _('Junior')
        SENIOR    = 'SR', _('Senior')
        GRADUATE  = 'GR', _('Graduate')


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    enroll = models.ForeignKey(Enroll, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=YearInSchool.choices
    )
