__author__ = 'tejawork'
from django.db import models
from shared.models import model_fields
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User)
    start_date = models.DateField()
    position_title = models.CharField(max_length=100)

    class Meta:
        app_label = "accounts"