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
        related_user = get_object_or_404(User, username=self.request.user)
        return queryset.filter(user=related_user)


    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CreateBookingSerializer
        return ListBookingSerializer

    @action(detail=True, methods=['post'])
    def cancelbooking(self, request, **kwargs):
        booking_to_cancel_id = request.data.get('booking_id')
        booking_to_cancel = get_object_or_404(booking,id=booking_to_cancel_id)
        booking_to_cancel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




