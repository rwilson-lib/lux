from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# from db_mixing import TimeStampMixin

class Address(models.Model):
    address_line_one = models.CharField(max_length=255)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    apt_building = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    providence = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.address_line_one

class Title(models.Model):
    title = models.CharField(max_length=255)
    abbr = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title if self.abbr is None else self.abbr

class Personal(models.Model):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    NOT_SAY = "X"

    MARRIED = "MA"
    WIDOWED = "WI"
    SEPARATED = "SE"
    DIVORCED = "DI"
    SINGLE = "SI"

    MARITAL_STATUS = [
        ( MARRIED, "Married" ),
        ( WIDOWED, "Widowed" ),
        ( DIVORCED, "Divorced" ),
        ( SINGLE, "Single" ),
    ]

    GENDER = [
        (MALE,"Male"),
        (FEMALE,"Female"),
        (OTHER, "Other"),
        (NOT_SAY, "Not Say")
    ]

    TITLES_SCHEMA = {
        "type" : "object",
        "properties" : {
            "title" : {
                "type" : "string"
            },
            "order" : {
                "type" : "number"
            }
        }
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titles = models.ManyToManyField(Title, through='PersonalTitle')
    first_name = models.CharField(max_length=255)
    given_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    maiden_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField(max_length=255)
    marital_status = models.CharField(max_length=2,  choices=MARITAL_STATUS, null=True, blank=True)
    skin_tone = models.CharField(max_length=255)
    eyes_color = models.CharField(max_length=255)
    height  = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    addresses = models.ManyToManyField(Address)

    def __str__(self):
        full_name = ""
        full_name += self.first_name

        if self.middle_name:
            full_name += " " + self.middle_name
        if self.maiden_name:
            full_name += " " + self.maiden_name
        else:
            full_name += " " + self.given_name

        return full_name


    def clean(self):
        errors={}
        if self.maiden_name is not None:
            if self.SINGLE == self.marital_status:
                errors['maiden_name'] = _('Not allow for Single')
            if self.gender is not self.FEMALE:
                errors['maiden_name'] = _('For female only')

        if errors:
            raise ValidationError(errors)

class PersonalTitle(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    order = models.IntegerField(null=True, blank=True)
