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

    def add_card(self, user, request):
        card = request.data
        created_card = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": card.number,
                "exp_month": card.exp_month,
                "exp_year": card.exp_year,
                "cvc": card.cvc,
            }
        )
        stripe.PaymentMethod.attach(
            created_card.id,
            user.stripe_id
        )

    def update_card(self, user):
        pass
    def delete_card(self, user):
        pass











