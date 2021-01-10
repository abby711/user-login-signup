from django.db import models



class newuser(models.Model):
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    namee=models.CharField(max_length=10)
