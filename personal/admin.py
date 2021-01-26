from django.contrib import admin

from .models import Personal
from .models import Address
from .models import Title
from .models import Contact
from .models import PersonalTitle
from .models import PersonalAddress
from .models import PersonalContact
from .models import Document
from .models import PersonalDocument

# Register your models here.


admin.site.register(Personal)

admin.site.register(Address)
admin.site.register(PersonalAddress)

admin.site.register(Contact)
admin.site.register(PersonalContact)

admin.site.register(Title)
admin.site.register(PersonalTitle)

admin.site.register(Document)
admin.site.register(PersonalDocument)
