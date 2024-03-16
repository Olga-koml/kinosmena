from django.contrib import admin
from .models import Shift


@admin.register(Shift)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'created']
