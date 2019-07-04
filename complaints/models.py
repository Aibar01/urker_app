from django.db import models
from employees.models import Employee


class Complaint(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.TextField()
    date_register = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(verbose_name='is good?')

    def __str__(self):
        return self.employee.name
