from django.db import models
from course import Course


class AssignmentType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, related_name="assignment_types")

    class Meta():
        app_label = "grades"