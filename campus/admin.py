from django.contrib import admin

# Register your models here.

from .models import Campus
from .models import Building
from .models import Room
from .models import CourseCampus
from .models import StaffCampus
from .models import CollegeCampus
from .models import SchoolCampus

admin.site.register(Campus)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(CourseCampus)
admin.site.register(StaffCampus)
admin.site.register(CollegeCampus)
admin.site.register(SchoolCampus)
