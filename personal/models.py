from django.db import models
from db_mixing import TimeStampMixin

# Create your models here.

class Personal(models.Model):
    GENDER = [
        ("M","MALE"),
        ("F","FEMALE"),
        ("O", "OTHER"),
        ("X", "NOT_SAY")
    ]
    titles = models.JSONField()
    first_name = models.CharField(max_length=255)
    given_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True)
    maiden_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField(max_length=255)
    skin_tone = models.CharField(max_length=255)
    eyes_color = models.CharField(max_length=255)
    height  = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return "{} {} {} {}".format(
            self.first_name,
            self.middle_name,
            self.given_name,
        )
