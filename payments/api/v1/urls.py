"""
API V1: Payments Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from payments.api.v1.views import CardViewSet, PaymentsViewSet
from payments.api.v1.webhooks import my_webhook_view


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'payments', PaymentsViewSet, basename='payments')
router.register(r'card', CardViewSet, basename='card',)




###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^stripe/$', my_webhook_view, name='stripe_webhook'),
]
