from django.contrib import admin
from .models import LabExperiment

@admin.register(LabExperiment)
class LabExperimentAdmin(admin.ModelAdmin):
    list_display = ('standard', 'experiment')
    list_filter = ('standard','subject')
    search_fields = ('standard', 'experiment', 'description','subject')
