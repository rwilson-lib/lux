from django.contrib import admin

from .models import College
from .models import Course
from .models import Enroll
from .models import Position
from .models import School
from .models import Staff
from .models import SchoolCourse
from .models import CollegeCourse
from .models import CourseInstructor # need to add school instructor

admin.site.register(College)
admin.site.register(Course)
admin.site.register(Enroll)
admin.site.register(Position)
admin.site.register(School)
admin.site.register(Staff)
admin.site.register(SchoolCourse)
admin.site.register(CollegeCourse)
admin.site.register(CourseInstructor)
