__author__ = 'tejawork'

from django.db import models
from assignment import Assignment
from course import Course


class Score(models.Model):
    scored_points = models.IntegerField()
    assignment = models.ForeignKey(Assignment)
    course = models.ForeignKey(Course)

    class Meta():
        app_label = "grades"