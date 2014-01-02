__author__ = 'tejawork'

from rest_framework import views
from accounts.serializers.serializers import UserOutputSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserCreateOrListView(views.APIView):

    def get(self, request, *args, **kwargs):
        serializer = UserOutputSerializer(User.objects.all())
        return Response(serializer.data)