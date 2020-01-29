from django.db import models
from django.utils import timezone
from accounts.models import Profile


is_new_choices = (
    (True, 'نو'),
    (False, 'دسته دوم')
)

class Books(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    sale_price = models.IntegerField(blank=False, verbose_name='Sale Price')
    price_on_book = models.IntegerField(blank=False, verbose_name='Price on Book')
    is_new = models.BooleanField(choices=is_new_choices)
    created_at = models.DateTimeField(default=timezone.now())
    last_modified = models.DateTimeField(default=timezone.now())