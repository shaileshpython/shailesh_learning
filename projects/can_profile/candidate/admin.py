from django.contrib import admin
from .models import *
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['username']

admin.site.register(Candidate, CandidateAdmin)
