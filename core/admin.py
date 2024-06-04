# core/admin.py

from django.contrib import admin
from .models import Doctorinfo, HealthFact

class DoctorinfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'specialty')

class HealthFactAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'plan_type')


admin.site.register(Doctorinfo, DoctorinfoAdmin)
admin.site.register(HealthFact, HealthFactAdmin)
