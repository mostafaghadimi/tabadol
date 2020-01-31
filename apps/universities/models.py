from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)
    lattitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name
    