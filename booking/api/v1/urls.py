"""
API V1: Booking Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from booking.api.v1.views import BookingViewSet

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'bookings', BookingViewSet)

###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
]
