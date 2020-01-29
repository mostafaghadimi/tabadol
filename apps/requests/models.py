from django.contrib.auth.models import User
from apps.books.models import Books

from django.db import models

STATUS_CHOICES = (
    (1, 'دیده نشده'),
    (2,'رد شده'),
    (3,'تایید شده')
) 

class Requests(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Owner')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Requester')
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default=1, choices=STATUS_CHOICES)
