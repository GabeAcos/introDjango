from django.contrib import admin

import visits
# Register your models here.
from .models import Visits

@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
    pass
