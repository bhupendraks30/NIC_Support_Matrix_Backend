from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number', 'gender', 'state', 'district', 'city', 'pin_code' ,'role')
    search_fields = ('full_name', 'email', 'mobile_number','role')

@admin.register(AddProject)
class AddProjectAdmin(admin.ModelAdmin):
    list_display = ('hod_full_name','how_mail', 'hod_contact', 'hod_department','hod_address','project_duration','project_tittle','project_budget','description','date_submitted','status')
    search_fields = ('hod_full_name', 'hod_contact','hod_department','project_tittle',)
