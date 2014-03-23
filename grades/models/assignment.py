__author__ = 'tejawork'

from django.db import models
from course import Course
from assignment_type import AssignmentType


class Assignment(models.Model):
    """ This task class represents assignments given to students """

    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='assignments')
    assignment_type = models.OneToOneField(AssignmentType)
    max_points = models.IntegerField()
    due_date = models.DateField()
    assigned_date = models.DateTimeField()

    class Meta():
        app_label = "grades"    