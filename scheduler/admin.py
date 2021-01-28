from django.contrib import admin

from .models import Schedule
from .models import Break


admin.site.register(Schedule)
admin.site.register(Break)
