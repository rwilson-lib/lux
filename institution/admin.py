from django.contrib import admin


from .models import Institution
from .models import InstitutionAddress
from .models import InstitutionContact
from .models import InstitutionDocument
from .models import ISCEDLevel
from .models import Program
from .models import ProgramMap

admin.site.register(Institution)
admin.site.register(ISCEDLevel)
admin.site.register(InstitutionAddress)
admin.site.register(InstitutionContact)
admin.site.register(InstitutionDocument)
admin.site.register(Program)
admin.site.register(ProgramMap)
