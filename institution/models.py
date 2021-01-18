from django.db import models
import uuid


from instructor.models import Instructor

class AcademicYear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    semester = models.CharField(max_length=25)
    start_year = models.DateField()
    end_year = models.DateField()


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    motto = models.CharField(max_length=25)
    type = models.CharField(max_length=255)

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


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.CharField(max_length=100)
    code = models.IntegerField(blank=True, null=True)


class Enroll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    year = models.DateField()
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=25)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    #-Schedule
