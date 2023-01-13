from django.contrib import admin
from .models import User,Expenses,Team,TeamDetails
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(User, UserAdmin)

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['name','amount','user']

admin.site.register(Expenses,ExpensesAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Team,TeamAdmin)

class TeamDetailsAdmin(admin.ModelAdmin):
    list_display = ['team_id']

admin.site.register(TeamDetails,TeamDetailsAdmin)



