from django.shortcuts import render,redirect
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm


def base(request):
    return render(request,'base.html')

def department_post(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/depart_post")
    else:
        form = DepartmentForm()        
    return render(request,'department.html',{'form':form})


def employee_post(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/emp_post")
    else:
        form = EmployeeForm()        
    return render(request,'employee.html',{'form':form})


def assign_employee(request):
    employees = Employee.objects.all()
    return render(request,'index.html',{'employees':employees})
