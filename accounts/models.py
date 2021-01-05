"""
Accounts Models
"""
###
# Libraries
###
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _


###
# Choices
###
MALE = 'male'
FEMALE = 'female'
OTHER = 'other'

GENDER_CHOICES = [
    (MALE, _(MALE)),
    (FEMALE, _(FEMALE)),
    (OTHER, _(OTHER)),
]

###
# Querysets
###


###
# Models
###
class User(AbstractUser):
    email = models.EmailField(
        verbose_name=('email adress'),
        unique=True,
    )

    name = models.CharField(
        verbose_name=('name'),
        max_length=64,
        null=True,
    )
    height = models.CharField(
        max_length=8,
        verbose_name=('height'),
        help_text=('in metres'),
        null=True,
    )
    weight = models.CharField(
        max_length=8,
        verbose_name=('weight'),
        help_text=('in kgs'),
        null=True,
    )
    date_of_birth = models.DateField(
        verbose_name=('date of birth'),
        null=True,
        blank=True,
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        verbose_name=('gender'),
        max_length=8,
        default=OTHER
    )
    address = models.CharField(
        verbose_name=('address'),
        max_length=64,
        null=True,
    )
    mobile_country_code = models.CharField(
        max_length=3,
        verbose_name=('code'),
        null=True,
    )
    mobile_phone_number = models.CharField(
        max_length=9,
        verbose_name=('number'),
        null=True,
    )

    stripe_id = models.CharField(
        max_length=32,
        verbose_name=('stripe'),
        null= False
    )




class ChangeEmailRequest(models.Model):
    # Helpers
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        verbose_name=_('uuid'),
    )

    # User model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='change_email_request',
        verbose_name=_('user'),
    )

    # Email
    email = models.EmailField(verbose_name=_('email'))
