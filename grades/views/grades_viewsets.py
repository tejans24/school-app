__author__ = 'tejawork'
from rest_framework import viewsets
from grades.models import Course, Assignment, Score
from grades.serializers import grades_serializers

class CourseViewSet(viewsets.ModelViewSet):
    model = Course
    serializer_class = grades_serializers.CourseSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    model = Assignment


class ScoreViewSet(viewsets.ModelViewSet):
    model = Score

