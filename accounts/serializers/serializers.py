
from accounts.models.users import UserProfile, Student
from rest_framework import serializers
from django.contrib.auth.models import User


class UserInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                  'is_active')

class UserOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                  'is_active')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    user = UserInputSerializer(source="user", read_only=True)

    class Meta:
        model = UserProfile


class StudentSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(source="user_profile", read_only=True)

    class Meta:
        model = Student
        fields = ('username', 'grade_level')

