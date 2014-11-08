from django.db import models
from django.contrib import admin
# Create your models here.

class Car(models.Model):
    car_type = (
        ('se', 'Sedan'),
        ('su', 'SUV'),
        ('ha', 'HashBack')
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=6, choices=car_type)
    ac = models.BooleanField(default=True)
    rent = models.IntegerField()
    image = models.ImageField(upload_to='/car/')


