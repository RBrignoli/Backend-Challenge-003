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

    def add_card(self, card_client, request):
        token = card_client
        card = stripe.Customer.create_source(
            request.user.stripe_id,
            source=token,
        )
        return card


    def list_cards(self, user):
        card_list = stripe.Customer.list_sources(
            user.stripe_id,
            object="card",
        )
        return card_list


    def delete_card(self, request):
        request_obj = request
        card_delete = stripe.Customer.delete_source(
            request_obj.user.stripe_id,
            request_obj.data.get('card')
        )
        return card_delete

    def token_create(self, request):
        request_obj = request
        request_data = request_obj.data
        token = stripe.Token.create(
            card={
                "number": request_data.get('number'),
                "exp_month": request_data.get('exp_month'),
                "exp_year": request_data.get('exp_year'),
                "cvc": request_data.get('exp_cvc'),
            },
        )
        return token




class StripePaymentClient:

    def list_payments(self, user):
        payments_list = stripe.PaymentIntent.list(customer=user.stripe_id)
        return payments_list










