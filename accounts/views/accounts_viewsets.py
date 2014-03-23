__author__ = 'tejawork'
from accounts.models.user import UserProfile
from django.contrib.auth.models import User
from rest_framework import viewsets


# ViewSets define the view behavior.
class UserProfileViewSet(viewsets.ModelViewSet):
    model = UserProfile


class UserViewSet(viewsets.ModelViewSet):
    model = User
