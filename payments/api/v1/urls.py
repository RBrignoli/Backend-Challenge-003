"""
API V1: Payments Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from payments.api.v1.views import CardViewSet, PaymentsViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'payments', PaymentsViewSet, basename='payments')
router.register(r'addcard', CardViewSet, basename='add_card',)



###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
]
