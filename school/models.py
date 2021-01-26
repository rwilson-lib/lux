from django.db import models
import uuid


from personal.models import Personal
from institution.models import Institution, ISCEDLevel
from instructor.models import Instructor
from student.models import Student


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


class AcademicYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    semester = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level = models.ManyToManyField(ISCEDLevel)
    title = models.CharField(max_length=100)
    code = models.PositiveIntegerField(blank=True, null=True)
    credit_hour = models.PositiveIntegerField(default=1)
    instructors = models.ManyToManyField(Instructor, through='CourseInstructor')

    def __str__(self):
        return "{} {} {}hr".format(self.title, self.code, self.credit_hour)

class CourseInstructor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)


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


class SchoolCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Enroll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=25, unique=True)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)


    def __str__(self):
        return self.id_number


class Postion(models.Model):
    postion = models.CharField(max_length=25)
    description = models.TextField()


class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    postions = models.ManyToManyField(Postion)
