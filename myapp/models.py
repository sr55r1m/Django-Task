from django.db import models

# Create your models here.

class Register(models.Model):
    username=models.CharField(max_length=50,null=True)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20,null=True)
