"""
Booking Signals
"""
###
# Libraries
###
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from helpers.stripe import StripeAccountClient
from helpers import stripe

from booking.models import Booking

###
# Signals
###

@receiver(post_save, sender=Booking)
def create_charge(sender, instance, **kwargs):
    created = kwargs.get("created")
    if created:
        charge = stripe.StripePaymentClient.charge(instance)
        if charge.paid:
            instance.charge_paid = True
            instance.charge_id = charge.id

        else:
            instance.canceled = True

        instance.save()










