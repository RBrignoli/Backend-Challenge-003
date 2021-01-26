"""
Payments Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class PaymentsConfig(AppConfig):
    name = 'payments'

    def ready(self):
        import payments.signals
