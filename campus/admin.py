from django.contrib import admin

# Register your models here.

from .models import Campus
from .models import Building
from .models import Room
from .models import CourseCampus
from .models import CampusStaff
from .models import CollegeCampus
from .models import SchoolCampus
from .models import ClassRoom

admin.site.register(Campus)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(CourseCampus)
admin.site.register(CampusStaff)
admin.site.register(CollegeCampus)
admin.site.register(SchoolCampus)
admin.site.register(ClassRoom)
