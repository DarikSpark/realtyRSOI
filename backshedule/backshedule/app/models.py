from django.db import models


class Shedule(models.Model):
    user_id = models.IntegerField(default=0)
    flat_id = models.IntegerField(default=0)
    date = models.DateField()
    date_to = models.DateField(default='2015-01-01')
    busy_from = models.TimeField()
    busy_to = models.TimeField()
