from django.db import models

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=64)
    body = models.CharField(max_length=256)

    image = models.ImageField()



