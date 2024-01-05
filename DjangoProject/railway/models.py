from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #OneToMany
from django.db.models import Sum
from django.urls import reverse
class train(models.Model):
    train_name=models.CharField(max_length=50) 
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50) 
    price=models.FloatField(default=120)
    arrival_time=models.TimeField()
    departure_time=models.TimeField()
    seats_available=models.IntegerField(default=100)
    running_days = models.CharField(max_length=50)
    
