from apps.universities.models import University
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE,
                                related_name= 'profile'
                                )
                                
    avatar = models.ImageField(upload_to='static/avatars', default='/')
    university = models.ForeignKey(University,
                                      on_delete=models.CASCADE,
                                      related_name='university'
                                     )
    discipline = models.CharField(max_length=100,
                                 default="", 
                                 verbose_name="field of study"
                                 )
    is_student = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.user.email)