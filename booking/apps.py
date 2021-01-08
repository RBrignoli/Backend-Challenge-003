"""
Booking Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class BookingConfig(AppConfig):
    name = 'booking'

    def ready(self):
        import booking.signals
