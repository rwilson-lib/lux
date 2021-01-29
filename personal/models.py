from django.core.exceptions import ValidationError
from django.core.validators import validate_email

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

class Suffix(models.Model):
    class Suffix(models.TextChoices):
        SENIOR = "SR", _('Sr.')
        JUNIOR = "JR", _('Jr.')
        FIRST = "01" , _('I')
        SECOND = "02", _('II')
        THIRD = "03", _('III')
        FOURTH = "04", _('IV')
        FIFTH = "05", _('V')
        SIX = "06", _('VI')
        SEVENTH = "07", _('VII')
        EIGHTH = "08", _('VIII')
        NINTH = "09", _('XI')
        TENTH = "10", _('X')
        REQUEST = "XX"

        __empty__ = "(NONE)"

    suffix = models.CharField(max_length=2, choices=Suffix.choices, null=True, blank=True)

    def __str__(self):
        return self.get_suffix_display()


class Contact(models.Model):
    type = models.CharField(max_length=25)
    value = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return "{}".format(self.value)

    def clean(self):
        self.type = str(self.type).lower()
        if  self.type == 'email':
            validate_email(self.value)


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
    label = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.address_line_one

class Document(models.Model):
    path = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True, blank=True, null=True)
    label = models.CharField(max_length=10, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    issuer = models.CharField(max_length=10, blank=True, null=True)
    validation_url = models.URLField(blank=True, null=True)
    validation_code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Personal(models.Model):
    class Gender(models.TextChoices):
        FEMALE = "F"
        MALE = "M"
        NOT_SAY = "X"
        OTHER = "O"

    class MaritalStatus(models.TextChoices):
        DIVORCED = "DI"
        MARRIED = "MA"
        SEPARATED = "SE"
        SINGLE = "SI"
        WIDOWED = "WI"
        __empty__ = "(NONE)"

    class EyesColor(models.TextChoices):
        AMBER = "AR"
        BLACK = "BK"
        BLUE = "BE"
        BROWN = "BN"
        GRAY = "GY"
        GREEN = "GN"
        HAZEL = "HL"
        RED_ALBINO = "RA"
        __empty__ = "(UNKNOWN)"

    class SkinColor(models.TextChoices):
        IVORY = 'IV'
        BEIGE = 'BE'
        ALABASTER = 'AB'
        HONEY = 'HO'
        CAROTENOID = 'CT'
        TAN = 'TA'
        CARAMEL = 'CA'
        BRONZE = 'BR'
        MAHOGANY = 'MA'
        CHESTNUT = 'CH'
        BUFF = 'BU'
        PEACHESCREAM = 'PC'
        UMBER = 'UM'
        PRALINE = 'PR'
        ESPRESSOBROWN = 'EB'
        PORCELAIN = 'PO'
        HICKORY = 'HI'
        MUSTARD = 'MU'
        SABLE = 'SA'
        ALMOND = 'AL'
        BISQUE = 'BI'
        TEAK = 'TE'
        CACAO = 'CC'
        PECAN = 'PE'
        SADDLEBROWN = 'SB'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=25)
    given_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    maiden_name = models.CharField(max_length=25, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices)
    date_of_birth = models.DateField(max_length=255)
    marital_status = models.CharField(max_length=2,  choices=MaritalStatus.choices, null=True, blank=True)
    skin_color = models.CharField(max_length=2, choices=SkinColor.choices, null=True, blank=True)
    eyes_color = models.CharField(max_length=2, choices=EyesColor.choices, null=True, blank=True)
    height  = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=2)

    titles = models.ManyToManyField(Title, through='PersonalTitle')
    suffixes = models.ManyToManyField(Suffix, through='PersonalSuffix')
    contacts = models.ManyToManyField(Contact, through='PersonalContact')
    addresses = models.ManyToManyField(Address, through='PersonalAddress')
    documents = models.ManyToManyField(Document, through='PersonalDocument')

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
            if self.Gender.SINGLE == self.marital_status:
                errors['maiden_name'] = _('Not allow for Single')
            if self.Gender.FEMALE is not self.gender:
                errors['maiden_name'] = _('For female only')

        if errors:
            raise ValidationError(errors)


class PersonalTitle(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    order = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        unique_together = ('personal','title')

class PersonalSuffix(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    suffix = models.ForeignKey(Suffix, on_delete=models.CASCADE)
    order = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        unique_together = ('personal','suffix')

class PersonalAddress(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    label = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ('personal','address')


class PersonalContact(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    label = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ('personal','contact')


class PersonalDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

