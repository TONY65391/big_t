from django.db import models

# Create your models here.

class MODELS(models.Model):
    id = models.IntegerField(null=False,default=True, primary_key=True)
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    phone = models.IntegerField(null=False, default=True, primary_key=False)
    Gmail = models.CharField(max_length=200)