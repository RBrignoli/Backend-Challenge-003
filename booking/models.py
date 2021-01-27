"""
Booking Models
"""
###
# Libraries
###
from datetime import datetime

from dateutil.relativedelta import relativedelta
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
        verbose_name=('start time'),
    )
    gym_end_time = models.TimeField(
        verbose_name=('end time'),
    )
    max_number_of_users= models.IntegerField(
        verbose_name=('max users'),
        validators = [MaxValueValidator],
        null = False,
        blank = False,
    )
    hourly_rate = models.DecimalField(
        verbose_name=('price'),
        validators = [MinValueValidator(0.0)],
        decimal_places=2,
        max_digits=6,
        null = False,
        blank = False,
    )


class Booking(models.Model):

    user = models.ForeignKey(
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
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name=('price'),
        validators=[MinValueValidator(0.0)],
        null = True,
        blank = True,
        decimal_places=2,
        max_digits=6,
    )
    charge_paid = models.BooleanField(
        default= False,
        verbose_name=('paid'),
    )
    canceled = models.BooleanField(
        default= False,
        verbose_name=('canceled'),
    )
    refound = models.BooleanField(
        default= False,
        verbose_name=('refound'),
    )
    charge_id = models.CharField(
        verbose_name=('charge'),
        max_length=30,
    )



    @staticmethod
    def simultaneus_users(start_time, end_prevision, date):
        return Booking.objects.filter(date=date).filter(Q(end_prevision__gte=start_time)).filter(Q(start_time__lte=end_prevision)).count()

    @property
    def duration(self):
        end = datetime.combine(self.date, self.end_prevision)
        start = datetime.combine(self.date, self.start_time)
        duration_booking = relativedelta(end, start)
        minutes = duration_booking.minutes
        hours = duration_booking.hours
        total_time = 60*hours + minutes
        return total_time


    @property
    def price(self):
        hourly_rate = Gym.objects.first().hourly_rate
        charge_price = self.duration * hourly_rate
        return charge_price




