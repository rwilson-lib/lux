from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid


from institution.models import ISCEDLevel
from scheduler.models import Schedule
from campus.models import ClassRoom
from campus.models import CampusStaff

from school.models import Course
from school.models import Enroll
from school.models import Instructor



class AcademicYear(models.Model):

    class Season(models.TextChoices):
        SUMMER = 'SU', _('Summer')
        WINTER = 'WI', _('Winter')
        AUTUMN = 'AU', _('Autumn')
        SPRING = 'SP', _('Spring')
        __empty__ = _('(Unknown)')

    class Semester(models.IntegerChoices):
        FIRST_SEMESTER = 1, _('1st Semester')
        SECOND_SEMESTER = 2, _('2nd Semester')
        THIRD_SEMESTER = 3, _('3rd Semester')


    class SemesterType(models.IntegerChoices):
        SEMESTER = 0
        TRIMESTER = 1

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.IntegerField(choices=SemesterType.choices)
    semester = models.IntegerField(choices=Semester.choices)
    season = models.CharField(max_length=2, choices=Season.choices)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return "{}-{}".format( self.start_date.year, self.end_date.year )


class AcademicStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=25)
    levels = models.ManyToManyField(ISCEDLevel)


class InstructorCourseSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('academic_year', 'course', 'instructor')


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    enrolls = models.ManyToManyField(Enroll)
    instructors = models.ManyToManyField( InstructorCourseSchedule )

    def __str__(self):
        return self.name


class GradeSchoolSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    enrolls = models.ManyToManyField(Enroll)
    instructor_course_schedules = models.ManyToManyField( InstructorCourseSchedule )
    sponsor = models.ForeignKey(CampusStaff, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
