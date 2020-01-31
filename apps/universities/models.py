from apps.accounts.models import Profile
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(Profile, related_name='profile', on_delete=models.CASCADE)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Universities'
