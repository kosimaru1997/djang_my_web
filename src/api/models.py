from django.db import models


# Create your models here.

class Question(models.Model):
    label = models.CharField(max_length=30)
    ask = models.CharField(max_length=30)
    answer = models.TextField
