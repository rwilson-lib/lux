from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from jsonschema import validate
from jsonschema.exceptions import ValidationError as JsonValidationError
# from db_mixing import TimeStampMixin

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
        ( SEPARATED, "Separated" ),
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

    titles = models.JSONField(null=True, blank=True)
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

    def __str__(self):
        return "{} {} {}".format(
            self.first_name,
            self.middle_name,
            self.given_name,
        )

    def clean(self):
        errors={}


        if self.maiden_name is not None:
            if self.SINGLE == self.marital_status:
                errors['maiden_name'] = _('Not allow for Single')
            if self.gender is not self.FEMALE:
                errors['maiden_name'] = _('For female only')

        if self.titles is not None:
            try:
                validate(instance=self.titles, schema=self.TITLES_SCHEMA)
            except JsonValidationError as e:
                print(self.titles)
                errors['titles']= _('bad title')

        if errors:
            raise ValidationError(errors)
