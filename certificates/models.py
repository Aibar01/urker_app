from django.db import models
from employees.models import Employee


class Certificate(models.Model):

    certificate = models.FileField(upload_to="certificates/")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.name


class Resume(models.Model):

    resume = models.FileField(upload_to="resumes/")
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.name


class Education(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_finished = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)