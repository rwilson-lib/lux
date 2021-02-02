from django.contrib import admin

from .models import AcademicQuarter
from .models import AcademicQuarterActivity
from .models import AcademicStatus
from .models import AcademicYear
from .models import Activity
from .models import InstructorCourseSchedule
from .models import QuarterSectionStudentAttendance
from .models import QuarterSectionStudentMark
from .models import Section
from .models import SectionInstructor
from .models import SectionStudent

admin.site.register(AcademicQuarter)
admin.site.register(AcademicQuarterActivity)
admin.site.register(AcademicStatus)
admin.site.register(AcademicYear)
admin.site.register(Activity)
admin.site.register(InstructorCourseSchedule)
admin.site.register(QuarterSectionStudentAttendance)
admin.site.register(QuarterSectionStudentMark)
admin.site.register(Section)
admin.site.register(SectionInstructor)
admin.site.register(SectionStudent)
