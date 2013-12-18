__author__ = 'tejawork'
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Student(User):

    class Meta:
        app_label = "grades"


class Teacher(User):

    class Meta:
        app_label = "grades"