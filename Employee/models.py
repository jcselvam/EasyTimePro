from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(default="")
    employee = models.CharField(max_length=50 , default="")
    employee_address = models.CharField(max_length=50, default="")
    department = models.ForeignKey("Department", default="", on_delete = models.CASCADE)

    def __str__(self):
        return self.employee


class Department(models.Model):
    department_id = models.CharField(max_length=50 , default="")
    department = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.department