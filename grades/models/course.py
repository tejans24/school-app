__author__ = 'tejawork'

from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    class_grade = models.IntegerField(blank=False)

    class Meta():
        app_label = "grades"