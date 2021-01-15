from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# from db_mixing import TimeStampMixin

class Title(models.Model):
    title = models.CharField(max_length=255)
    abbr = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title if self.abbr is None else self.abbr

class Personal(models.Model):
    FEMALE = "F"
    MALE = "M"
    NOT_SAY = "X"
    OTHER = "O"

    DIVORCED = "DI"
    MARRIED = "MA"
    SEPARATED = "SE"
    SINGLE = "SI"
    WIDOWED = "WI"

    AMBER = "AR"
    BLACK = "BK"
    BLUE = "BE"
    BROWN = "BN"
    GRAY = "GY"
    GREEN = "GN"
    HAZEL = "HL"
    RED_ALBINO = "RA"

    MARITAL_STATUS = [
        ( MARRIED, "Married" ),
        ( WIDOWED, "Widowed" ),
        ( DIVORCED, "Divorced" ),
        ( SINGLE, "Single" ),
    ]

    EYES_COLORS = [
        (AMBER, "Amber"),
        (BLACK, "Black"),
        (BLUE, "Blue"),
        (BROWN, "Brown"),
        (GRAY, "Gray"),
        (GREEN, "Green"),
        (HAZEL, "Hazel"),
        (RED_ALBINO, "Red Albino")
    ]

    GENDER = [
        (MALE,"Male"),
        (FEMALE,"Female"),
        (OTHER, "Other"),
        (NOT_SAY, "Not Say")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=255)
    given_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    maiden_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField(max_length=255)
    marital_status = models.CharField(max_length=2,  choices=MARITAL_STATUS, null=True, blank=True)
    skin_tone = models.CharField(max_length=255, null=True, blank=True)
    eyes_color = models.CharField(max_length=2, choices=EYES_COLORS, null=True, blank=True)
    height  = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255)

    titles = models.ManyToManyField(Title, through='PersonalTitle')

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

class Address(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=255)
    address_line_two = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    apt_building = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    providence = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2)
    label = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.address_line_one


class PersonalTitle(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    order = models.IntegerField(null=True, blank=True)
