from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='appname', null=True)
    writer= models.CharField(null=False,max_length=50)
    title= models.CharField(null=False,max_length=50)