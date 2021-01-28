from django.db import models
import uuid

# Create your models here.


class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    sunday_start = models.TimeField(blank=True, null=True)
    sunday_end = models.TimeField(blank=True, null=True)
    monday_start = models.TimeField(blank=True, null=True)
    monday_end = models.TimeField(blank=True, null=True)
    tueday_start = models.TimeField(blank=True, null=True)
    tueday_end = models.TimeField(blank=True, null=True)
    wednesday_start = models.TimeField(blank=True, null=True)
    wednesday_end = models.TimeField(blank=True, null=True)
    thursday_start = models.TimeField(blank=True, null=True)
    thursday_end = models.TimeField(blank=True, null=True)
    friday_start = models.TimeField(blank=True, null=True)
    friday_end = models.TimeField(blank=True, null=True)
    saturday_start = models.TimeField(blank=True, null=True)
    saturday_end = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Break(models.Model):
    name = models.CharField(max_length=25)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    start_at = models.TimeField(blank=True, null=True)
    end_at = models.TimeField(blank=True, null=True)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)

    def __str__(self):
        return "{} => {}".format(self.name, self.schedule.name)
