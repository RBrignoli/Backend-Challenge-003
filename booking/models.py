"""
Booking Models
"""
###
# Libraries
###
from django.db import models
from django.db.models import Q
from helpers.models import TimestampModel
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import User

###
# Choices
###


###
# Querysets
###


###
# Models
###

class Gym(models.Model):

    gym_start_time = models.TimeField(
        verbose_name=('start time')
    )
    gym_end_time = models.TimeField(
        verbose_name=('end time')
    )
    max_number_of_users= models.IntegerField(
        verbose_name=('max users'),
        validators = [MaxValueValidator],
        null = False,
        blank = False
    )
    hourly_rate = models.DecimalField(
        verbose_name=('price'),
        validators = [MinValueValidator(0.0)],
        null = False,
        blank = False
    )


class Booking(models.Model):

    user = models.OneToOneField(
        User,
        verbose_name=('user'),
        related_name=('user'),
        on_delete=models.CASCADE,
    )
    start_time = models.TimeField(
        verbose_name=('start time'),
    )
    end_prevision = models.TimeField(
        verbose_name=('end time'),
    )
    date = models.DateField(
        verbose_name=('date'),
    )
    duration = models.TimeField(
        verbose_name=('duration'),
    )
    price = models.DecimalField(
        verbose_name=('price'),
        validators=[MinValueValidator(0.0)],
        null = True,
        blank = True,
    )
    charge_paid = models.BooleanField(
        default= False,
        verbose_name=('charge')
    )
    canceled = models.BooleanField(
        default= False,
        verbose_name=('canceled')
    )
    refound = models.BooleanField(
        default= False,
        verbose_name=('refound')
    )



    @staticmethod
    def simultaneus_users(start_time, end_prevision, date):
        return Booking.objects.filter(date=date).filter(Q(end_time__gte=start_time)).filter(Q(start_time__lte=end_prevision)).count()



