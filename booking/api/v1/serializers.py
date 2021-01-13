"""
API V1: Booking Serializers
"""
###
# Libraries
###

from booking.models import Booking
from settings.settings import MAX_NUMBER_OF_USERS, GYM_START_TIME, GYM_END_TIME, GYM_HOURLY_RATE

from rest_framework import serializers

###
# Serializers
###


class CreateBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('user', 'start_time', 'end_prevision', 'date')

    def validate(self, obj):




class ListBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('user', 'start_time', 'end_prevision', 'date','duration', 'price', 'charge_paid', 'refound', 'canceled')

