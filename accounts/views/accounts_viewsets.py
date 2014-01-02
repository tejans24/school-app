__author__ = 'tejawork'
from rest_framework import viewsets
from accounts.serializers.serializers import StudentSerializer, UserProfileSerializer
from accounts.models import Student, Teacher
from accounts.models.users import UserProfile
from django.contrib.auth.models import User
from accounts.serializers.serializers import UserInputSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    model = UserProfile
    serializer_class = UserProfileSerializer

class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    serializer_class = StudentSerializer

class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserInputSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    model = Teacher