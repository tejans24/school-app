__author__ = 'tejawork'
from rest_framework import viewsets
from grades.models import Course, Assignment, Score


class CourseViewSet(viewsets.ModelViewSet):
    model = Course


class AssignmentViewSet(viewsets.ModelViewSet):
    model = Assignment


class ScoreViewSet(viewsets.ModelViewSet):
    model = Score

