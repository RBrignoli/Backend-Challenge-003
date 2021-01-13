"""
Booking admin
"""
###
# Libraries
###
from django.contrib import admin
from booking.models import Booking, Gym

###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_time', 'end_prevision', 'date', 'charge_paid',]
    list_filter = ['user', 'date',]
    fieldsets = (
        (('Booking'),
         {'fields': ('user', 'start_time', 'end_prevision', 'date', 'charge_paid',)}),
    )

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['gym_start_time', 'gym_end_time', 'max_number_of_users', 'hourly_rate',]
    def has_add_permission(self, request):
        if not Gym.objects.exists():
            return True
        else:
            return False
