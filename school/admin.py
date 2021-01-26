from django.contrib import admin

from .models import AcademicYear
from .models import College
from .models import Course
from .models import Enroll
from .models import Postion
from .models import School
from .models import Staff
from .models import SchoolCourse
from .models import CollegeCourse
from .models import CourseInstructor # need to add school instructor

admin.site.register(AcademicYear)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Enroll)
admin.site.register(Postion)
admin.site.register(School)
admin.site.register(Staff)
admin.site.register(SchoolCourse)
admin.site.register(CollegeCourse)
admin.site.register(CourseInstructor)
