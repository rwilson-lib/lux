from django.contrib import admin

from .models import Personal
from .models import Address
from .models import Title
from .models import PersonalTitle

# Register your models here.


admin.site.register(Personal)
admin.site.register(Title)
admin.site.register(Address)
admin.site.register(PersonalTitle)
