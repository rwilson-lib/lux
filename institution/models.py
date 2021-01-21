from django.db import models
import uuid


from instructor.models import Instructor


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)

class ISCEDLevel(models.Model):
    level =  models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    year = models.DateField()
    description = models.TextField()

class AcademicYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    semester = models.CharField(max_length=25)
    start_year = models.DateField()
    end_year = models.DateField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    motto = models.CharField(max_length=25)
    mascot = models.ImageField()
    levels = models.ManyToManyField(ISCEDLevel, on_delete=models.CASCADE)
    year_founded = models.DateField()

    def __str__(self):
        return self.name



class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    motto = models.CharField(max_length=25)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Campus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25, default="")
    elevation =  models.IntegerField(blank=True, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    floor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=25)


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.CharField(max_length=100)
    code = models.IntegerField(blank=True, null=True)
    credit_hour = models.PositiveIntegerField(default=1)


class InstructorCourse(models.Model):
    instructor = models.ManyToManyField(Instructor)
    course = models.ManyToManyField(Course)
    xp = models.IntegerField(blank=True, null=True)


class Enroll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    year = models.DateField()
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)


class ClassRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    _class = models.ManyToManyField(Class, on_delete=models.CASCADE)
    room = models.ManyToManyField(Room, on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=25)
    classroom = models.ForeignKey(Course, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    #-AcademicYear
    #-Schedule

class SectionEnrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    enroll = models.ForeignKey(Enroll, on_delete=models.CASCADE)
