from django.contrib import admin

from .models import Personal
from .models import Address
from .models import Title
from .models import PersonalTitle
from .models import Contact

# Register your models here.


admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Personal)
admin.site.register(PersonalTitle)
admin.site.register(Title)
