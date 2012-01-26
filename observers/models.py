from django.db import models

class Observer(models.Model):
    full_name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    info = models.TextField()
    in_moscow = models.BooleanField()
