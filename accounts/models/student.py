__author__ = 'tejawork'
from django.db import models
from shared.models import model_fields
from accounts.models.address import Address
from accounts.models.guardian import Guardian
from django.contrib.auth.models import User
import constants


class Student(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    student_id = models.CharField(max_length=100)
    current_grade_level = model_fields.IntegerRangeField(min_value=0, max_value=12, help_text='Student grade level.')
    address = models.OneToOneField(Address)
    parent = models.ForeignKey(Guardian, null=True)
    gender = models.CharField(max_length=1, choices=constants.GENDER_CHOICES, null=True)

    class Meta:
        app_label = "accounts"