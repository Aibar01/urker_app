from django.db import models
from datetime import datetime
from _decimal import ROUND_DOWN
from decimal import Decimal

class Position(models.Model):
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.position


class Employee(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name="Is it active?")
    image = models.ImageField(upload_to='employee/year-%Y/month-%m/day-%d', blank=True)
    about = models.TextField(verbose_name="History")
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=200, null=True)
    hire_date = models.DateField(default=datetime.now)

    @property
    def zero_id(self):
        id = f'{self.id:05}'
        return id

    @property
    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25)

    @property
    def rating_count(self):
        rating = 10
        plus = self.complaint_set.filter(status=True).count() * Decimal('0.2').quantize(Decimal('.1'), rounding=ROUND_DOWN)
        minus = self.complaint_set.filter(status=False).count() * Decimal('0.2').quantize(Decimal('.1'), rounding=ROUND_DOWN)

        rating -= minus
        rating += plus

        if rating > 10.0:
            rating = 10.0

        if rating <= 0.0:
            self.is_active = False

        return rating

    def __str__(self):
        return f'{self.id:05}' + " - " + self.name.title() + " " + self.surname.title()

