from django.db import models


class Game(models.Model):
    title = models.CharField(max_length= 255)
    taken = models.BooleanField()
    description = models.CharField(max_length=40000)
    price = models.FloatField()
    picture_url = models.CharField(max_length=2083, default='')


