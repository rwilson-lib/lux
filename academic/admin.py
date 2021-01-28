from django.contrib import admin

from .models import AcademicYear
from .models import GradeSchoolSection
from .models import InstructorCourseSchedule
from .models import Section

admin.site.register(AcademicYear)
admin.site.register(GradeSchoolSection)
admin.site.register(InstructorCourseSchedule)
admin.site.register(Section)

