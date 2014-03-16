author__ = 'tejawork'
from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = USStateField()
    zipcode = models.CharField(max_length=5)

    class Meta:
        app_label = "accounts"
