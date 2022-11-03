
from django.urls import path
from . import views

urlpatterns = [
    path("",views.base,name = 'base'),
    path("assign_employee",views.assign_employee,name = 'assign_employee'),
    path('depart_post', views.department_post, name='department_post'),
    path('emp_post', views.employee_post, name='employee_post'),  
]
