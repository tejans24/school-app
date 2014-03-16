__author__ = 'tejawork'

from django.db import models
from assignment import Assignment


class Score(models.Model):
    scored_points = models.IntegerField()
    assignment = models.ForeignKey(Assignment)

    class Meta():
        app_label = "grades"
