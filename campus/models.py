from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


import uuid


from personal.models import Address
from institution.models import Institution
from assembly.models import Class

from school.models import Staff
from school.models import Course
from school.models import College
from school.models import School


class Campus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    schools = models.ManyToManyField(School, through='SchoolCampus')

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



class ClassRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self._class.name, self.room.name)


class SchoolCampus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.school.name, self.campus.name)


class CollegeCampus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.college.name, self.campus.name)



class CourseCampus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.course.name, self.campus.name)

class CampusStaff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.campus.name)
