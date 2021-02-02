from django.db import models
import uuid


class Scope(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)


class Hook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)


class Requirement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    link_to = models.CharField(max_length=100)
    pointer = models.CharField(max_length=100)

    def __str__(self):
        return "{} -# {} -> {}".format(self.name, self.link_to, self.pointer)


class Assembly(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    scopes = models.ManyToManyField(Scope)
    hooks = models.ManyToManyField(Hook)
    requirements = models.ManyToManyField(Requirement)

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
