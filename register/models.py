from django.db import models
from django.utils import timezone


class Usersinfo(models.Model):
    username= models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100,default="1111")
    published=models.DateTimeField("published at", default=timezone.now())
    

    
