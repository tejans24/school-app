__author__ = 'tejawork'
from django.db import models
from django.contrib.auth.models import User
from phone import PhoneInfo


class Guardian(models.Model):
    user = models.OneToOneField(User)
    employer = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    
    class Meta:
        app_label = "accounts"