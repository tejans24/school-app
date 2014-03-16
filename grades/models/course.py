__author__ = 'tejawork'

from django.db import models
from accounts.models.student import Student
from accounts.models.teacher import Teacher


class Course(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    class_grade = models.IntegerField(blank=False)
    room_number = models.CharField(max_length=20)
    max_capacity = models.IntegerField()
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)

    class Meta():
        app_label = "grades"