from django.contrib import admin
from .models import JobPosition, Employee, EmployeeContract, Department

# Register your models here.
class JobPositionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'job_description',
        'no_employee',
        'date_created',
    )
    
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'manager',
        'date_created',
    )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'dept',
        'job_position',
        'dept_coach',
        'level',
        'badge_id',
        'next_appraisal',
    )
    
class EmployeeContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'contract_reference',
        'employee',
        'department',
        'job_position',
        'acc_no',
        'bank_name',
        'salary_type',
        'salary_details',
        'start_date',
        'status',        
    )

admin.site.register(EmployeeContract, EmployeeContractAdmin)
admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)