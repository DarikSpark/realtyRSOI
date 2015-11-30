from django.db import models


class Flat(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(default=0)
    rooms = models.IntegerField(default=0)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    user_id = models.IntegerField(default=0)

