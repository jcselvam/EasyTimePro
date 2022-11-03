from django.contrib import admin
from . models import Employee, Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department_id','department')

@admin.action(description='assign employee')
def assigned_employee(modeladmin,request,Department):
    Department.update( employee_address = 'bangalore')


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['employee_id','employee','employee_address','department']
    actions = [assigned_employee]  


admin.site.register(Employee,EmployeeAdmin)   
admin.site.register(Department,DepartmentAdmin)    