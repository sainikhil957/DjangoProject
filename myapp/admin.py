from django.contrib import admin

# Register your models here.
from .models import Fdsignup
from .models import Cusignup
from .models import Fdform
from .models import Cuitems


admin.site.register(Fdsignup)
admin.site.register(Cusignup)
admin.site.register(Fdform)
admin.site.register(Cuitems)