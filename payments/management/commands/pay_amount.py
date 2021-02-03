from django.core.management import BaseCommand
from helpers import stripe


class Command(BaseCommand):
    def handle(self, *args, **options):
        balance = stripe.StripePayout.balance()
        amount = balance.amount
        payout = stripe.StripePayout.payout(balance)
