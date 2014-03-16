__author__ = 'tejawork'
from django.contrib.auth.models import User
from django.db import models
from shared.models import model_fields

class UserProfile(models.Model):

    USER_TYPES = (
        ('S', 'Student'),
        ('T', 'Teacher'),
        ('PA', 'Parent'),
        ('PR', 'Principle'),
        ('A', 'Admin'),
    )

    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=2, choices=USER_TYPES)

    class Meta:
        app_label = "accounts"

    def __unicode__(self):
        return self.user.username