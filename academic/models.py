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

from assembly.models import Class


class AcademicYear(models.Model):
    class Season(models.TextChoices):
        SUMMER = 'SU', _('Summer/Dry')
        SPRING = 'SP', _('Spring/Rainy')
        WINTER = 'WI', _('Winter')
        AUTUMN = 'AU', _('Autumn')
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

    def __str__(self):
        return "{} {} {} {}".format(self.academic_year, self.course, self.instructor, self.classroom)


class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    section = models.CharField(max_length=2)
    _Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(InstructorCourseSchedule, through='SectionInstructor')
    students = models.ManyToManyField(Enroll, through='SectionStudent')

    def __str__(self):
        return "[{}] {}".format(self._Class.name, self.name)

    class Meta:
        unique_together = ('academic_year','section', '_Class')


class SectionStudent(models.Model):
    class Status(models.TextChoices):
        PASSED      =  'PASS'
        FAILED      =  'FAIL'
        REMINDER    =  'REMI'
        INCOMPLETE  =  'INCO'
        NOGRADE     =  'NOGR'
        DROP        =  'DROP'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    student = models.ForeignKey(Enroll, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('academic_year', 'section', 'student')

    def __str__(self):
        return "{} | {} | {}".format(self.academic_year, self.section, self.student)


class Leadership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    postion = models.CharField(max_length=25)


class SectionStudentLeadership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(SectionStudent, on_delete=models.CASCADE)
    Leadership = models.ForeignKey(Leadership, on_delete=models.CASCADE)


class SectionGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.CharField(max_length=25)


class SectionInstructor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    instructor_course_schedules = models.ForeignKey(InstructorCourseSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.section, self.instructor_course_schedules)


class SectionInstructorLeadership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instructor = models.ForeignKey(SectionInstructor, on_delete=models.CASCADE)
    Leadership = models.ForeignKey(Leadership, on_delete=models.CASCADE)


class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity = models.CharField(max_length=25)
    point = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} {}".format(self.activity, self.point)


class AcademicQuarter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    quater = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} {}".format(self.academic_year, self.quater)


class AcademicQuarterActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quater = models.ForeignKey(AcademicQuarter, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    section_instruction = models.ForeignKey(SectionInstructor, on_delete=models.CASCADE)
    point = models.DecimalField(max_digits=5, decimal_places=2)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)


class QuarterSectionStudentMark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(SectionStudent, on_delete=models.CASCADE)
    quater_activity = models.ForeignKey(AcademicQuarterActivity, on_delete=models.CASCADE)
    point = models.DecimalField(max_digits=5, decimal_places=2)


class QuarterSectionStudentAttendance(models.Model):
    class Absent(models.IntegerChoices):
        WITH_EXCUSE = 0
        WITHOUT_EXCUSE = 1
        SUBSPENDED = 2
        OTHER = 3

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(SectionStudent, on_delete=models.CASCADE)
    absent = models.IntegerField(choices=Absent.choices)
    date = models.DateField()
