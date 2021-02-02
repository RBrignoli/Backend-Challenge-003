"""
Booking admin
"""
###
# Libraries
###
from datetime import datetime


from django.contrib import admin
from django.core.exceptions import ValidationError

from booking.models import Booking, Gym
from helpers import stripe

###
# Inline Admin Models
###

admin.site.disable_action('delete_selected')

def cancel_booking(modeladmin, request, queryset):

    for booking in queryset:
        hour = booking.start_time
        date = booking.date
        time = datetime.combine(date, hour)
        if time < datetime.now():
            return ValidationError('date: you cant cancel a booking that already started/passed')
        if booking.charge_paid:
            refund = stripe.StripePaymentClient.refound(booking)
        if refund.status == 'succeeded':
            queryset.update(refound = True, canceled = True)
    cancel_booking.short_description = "cancel selected bookings"


###
# Main Admin Models
###
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'duration', 'date', 'price',  'charge_paid',]
    list_filter = ['user', 'date',]
    fieldsets = (
        (('Booking'),
         {'fields': ('user', 'start_time', 'end_prevision', 'date','charge_paid','canceled', 'refound')}),
    )
    actions = [cancel_booking]




@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['gym_start_time', 'gym_end_time', 'max_number_of_users', 'hourly_rate',]
    def has_add_permission(self, request):
        if not Gym.objects.exists():
            return True
        else:
            return False
