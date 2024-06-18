from django.contrib import admin
from .models import NnaUser, NnaCategory, NnaFAQ

admin.site.register(NnaUser)
admin.site.register(NnaCategory)
admin.site.register(NnaFAQ)
