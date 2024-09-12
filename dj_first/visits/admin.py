from django.contrib import admin

import visits
# Register your models here.
from .models import Visit

@admin.register(Visit)
class VisitsAdmin(admin.ModelAdmin):
    pass
