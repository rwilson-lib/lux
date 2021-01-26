from django.db import models
import uuid


from personal.models import Personal



class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)

    def __str__(self):
        return self.personal.__str__()
