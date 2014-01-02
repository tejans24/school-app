__author__ = 'tejawork'
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    class Meta:
        app_label = "accounts"


class Student(UserProfile):

    grade_level = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user.username

    class Meta:
        app_label = "accounts"


class Teacher(UserProfile):


    class Meta:
        app_label = "accounts"