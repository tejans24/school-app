__author__ = 'tejawork'

from django.db import models
from course import Course
from accounts.models.users import Teacher


class Assignment(models.Model):
    """ This task class represents assignments given to students """

    TERMS = (
        ('T', 'Test'),
        ('Q', 'Quiz'),
        ('H', 'Homework'),
        ('O', 'Other')
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TERMS, blank=False)
    course = models.ForeignKey(Course)
    max_points = models.IntegerField()
    due_date = models.DateField()
    assigned_date = models.DateField()
    teacher = models.ForeignKey(Teacher)

    class Meta():
        app_label = "grades"