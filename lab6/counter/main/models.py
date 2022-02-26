from django.db import models

# Create your models here.

class Count(models.Model):
    item = models.TextField()
    count = models.IntegerField()
