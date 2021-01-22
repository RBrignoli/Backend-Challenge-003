"""
Accounts Signals
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from helpers.stripe import StripeAccountClient

from accounts.models import User

###
# Signals
###



@receiver(post_save, sender=User)
def create_stripe_account(sender, instance, **kwargs):
    created = kwargs.get("created")
    if created:
        stripe_client = StripeAccountClient()
        stripe_account = stripe_client.create_stripe_account(instance)