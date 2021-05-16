from django.db import models


# Create your models here.
class ModelCV(models.Model):
    def __str__(self):
        return self.role
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    summary = models.TextField(max_length=2000)
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    current_role = models.CharField(max_length=1000)
    skills = models.TextField(max_length=5000)
