from django.contrib import admin
from .models import Employee,Job



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
        list_display = ['First_name','last_name','gender']

    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name']
