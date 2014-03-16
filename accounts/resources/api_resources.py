__author__ = 'tejawork'

from accounts.models.address import Address
from tastypie.resources import ModelResource
from tastypie.validation import Validation
from django.contrib.auth.models import User
from tastypie import fields
from accounts.models.student import Student
from tastypie.authorization import Authorization


class AddressResource(ModelResource):

    class Meta:
        queryset = Address.objects.all()
        resource_name = 'address'
        authorization = Authorization()
        include_resource_uri = False


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'email', 'first_name', 'last_name', 'last_login', 'user_type']
        authorization = Authorization()
        validation = Validation()


class StudentResource(ModelResource):

    address = fields.OneToOneField(AddressResource, 'address', full=True)
    user = fields.OneToOneField(UserResource, 'user')

    class Meta:
        queryset = Student.objects.all()
        resource_name = 'student'
        authorization = Authorization()



