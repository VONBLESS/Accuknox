from django.db import models

# Create your models here.
from django.db import models


class Accuknox(models.Model):
    name = models.CharField(max_length=120)


class AccuknoxMessage(models.Model):
    message = models.TextField()
