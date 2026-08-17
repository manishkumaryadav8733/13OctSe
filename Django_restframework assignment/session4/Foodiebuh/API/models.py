from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    location = models.CharField(max_length=255, default="Unknown")


    def __str__(self):
        return self.name
