#### Library ####


import stripe
from settings import settings




#### Actions ####


#create account
#add card
#delete card
#create charge
#refound

stripe.api_key = settings.STRIPE_API_KEY

class StripeAccountClient:

    def create_stripe_account(self, user):

        account = stripe.Customer.create(email=user.email, description= f'{user.name}#{user.id}')
        user.stripe_id = account.id
        user.save()


    def update_stripe_account(self, user):
        pass

    def delete_stripe_account(self, user):
        pass

    def list_stripe_costumers(self, user):
        pass


class StripeCardClient:

    def add_card(self, request):
        card = request
        created_card = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": card.data.number,
                "exp_month": card.data.exp_month,
                "exp_year": card.data.exp_year,
                "cvc": card.data.cvc,
            }
        )
        stripe.PaymentMethod.attach(
            created_card.id,
            request.user.stripe_id
        )

    def update_card(self, user):
        pass
    def delete_card(self, user):
        pass


class StripePaymentClient:

    def list_payments(self, user):
        payments_list = stripe.PaymentIntent.list(customer=user.stripe_id)
        return payments_list










