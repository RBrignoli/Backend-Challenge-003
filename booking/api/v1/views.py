"""
API V1: Booking Views
"""
###
# Libraries
###
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from booking.models import Booking
from booking.api.v1.serializers import CreateBookingSerializer, ListBookingSerializer

###
# Filters
###


###
# Viewsets
###
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()


    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CreateBookingSerializer
        return ListBookingSerializer

