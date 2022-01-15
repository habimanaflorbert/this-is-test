from django.db import models
from django.contrib.auth.models import User,auth
from django.conf import settings
# Create your models here.

class Information(models.Model):
    speed=models.DecimalField( max_digits = 5, decimal_places = 2)
    time=models.TimeField()
    date=models.DateField()
    distance=models.DecimalField( max_digits = 5, decimal_places = 2)
    description=models.TextField()
