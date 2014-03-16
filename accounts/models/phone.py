__author__ = 'tejawork'
from django.db import models
from localflavor.us.models import PhoneNumberField
import constants


class PhoneInfo(models.Model):
    phone_number = PhoneNumberField()
    phone_type = models.CharField(max_length=2, choices=constants.PHONE_NUMBER_TYPE)

    class Meta:
        app_label = "accounts"