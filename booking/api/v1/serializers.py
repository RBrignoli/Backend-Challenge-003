"""
API V1: Booking Serializers
"""
###
# Libraries
###
from datetime import datetime

from booking.models import Booking, Gym
from rest_framework.exceptions import ValidationError

from rest_framework import serializers


###
# Serializers
###


class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('start_time', 'end_prevision', 'date')
        read_only_fields = ('user', 'duration', 'price', 'charge_paid', 'canceled', 'refound',)

    def validate(self, attrs):
        start = attrs.get('start_time')
        start_gym = Gym.objects.first().gym_start_time
        if start < start_gym:
            raise ValidationError({'start_time': ('Cannot start before the GYM')})
        end = attrs.get('end_prevision')
        end_gym = Gym.objects.first().gym_end_time
        if end > end_gym:
            raise ValidationError({'end_prevision': ('Cannot end after the GYM')})
        if start > end:
            raise ValidationError({'end_prevision': ('Cannot end before starts')})
        booking_date = attrs.get('date')
        current_date = datetime.now().date()
        if booking_date < current_date:
            raise ValidationError({'date': ('invalid date')})
        max_users = Gym.objects.first().max_number_of_users
        simultaneus_users = Booking.simultaneus_users(start, end, booking_date)
        if simultaneus_users == max_users:
            raise ValidationError('Gym at max number of users')

        return attrs


class ListBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
        'user', 'start_time', 'end_prevision', 'date', 'duration', 'price', 'charge_paid', 'refound', 'canceled')
