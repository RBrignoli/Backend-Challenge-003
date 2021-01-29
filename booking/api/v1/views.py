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
from rest_framework.generics import get_object_or_404
from datetime import datetime

import stripe
from helpers import stripe

from booking.models import Booking
from accounts.models import User
from booking.api.v1.serializers import CreateBookingSerializer, ListBookingSerializer

###
# Filters
###


###
# Viewsets
###
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)


    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CreateBookingSerializer
        return ListBookingSerializer


    def perform_create(self, serializer):
            serializer.save(user=self.request.user)







    @action(detail=True, methods=['post'], url_path='cancel-booking',)
    def cancelbooking(self, request, **kwargs):

        booking_to_cancel_date = request.data.get("date")
        booking_to_cancel_starttime = request.data.get("start_time")
        time = datetime.combine(booking_to_cancel_date, booking_to_cancel_starttime)
        if time < datetime.now():
            return ValidationError('date: you cant cancel a booking that already started/passed')
        booking_to_cancel = get_object_or_404(Booking, date=booking_to_cancel_date, start_time=booking_to_cancel_starttime)
        booking_to_cancel.canceled = True
        if booking_to_cancel.charge_paid:
            refound = stripe.StripePaymentClient.refound(booking_to_cancel)
            if refound.status == 'succeeded':
                booking_to_cancel.refound = True
                booking_to_cancel.save()
        return Response(refound, status=status.HTTP_204_NO_CONTENT)






