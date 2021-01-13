"""
Booking admin
"""
###
# Libraries
###
from django.contrib import admin
from booking.models import Booking, Gym
from dateutil.relativedelta import relativedelta
from datetime import datetime

###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'duration', 'date', 'charge_paid',]
    list_filter = ['user', 'date',]
    fieldsets = (
        (('Booking'),
         {'fields': ('user', 'start_time', 'end_prevision', 'date','price','charge_paid','canceled', 'refound')}),
    )

    #prepopulated_fields = {'duration': }




@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['gym_start_time', 'gym_end_time', 'max_number_of_users', 'hourly_rate',]
    def has_add_permission(self, request):
        if not Gym.objects.exists():
            return True
        else:
            return False
