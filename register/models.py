from django.db import models


class Usersinfo(models.Model):
    username= models.CharField(max_length=100)
    pssword=models.CharField(max_length=100,default="1111")
    published=models.DateTimeField("published at")
    

    
