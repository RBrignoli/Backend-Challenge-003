"""
API V1: Payments Views
"""
###
# Libraries
###
from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from helpers.stripe import StripeCardClient, StripePaymentClient

from payments.api.v1.serializers import CreateCardSerializer


###
# Filters
###


###
# Viewsets
###


class PaymentsViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        payment_list = StripePaymentClient.list_payments(self, user)
        return Response(payment_list, status=status.HTTP_200_OK)


class CardViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateCardSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        card_client = StripeCardClient.token_create(self, request)
        card = StripeCardClient.add_card(self, card_client, request)
        return Response(card, status=status.HTTP_201_CREATED)

    def list(self, request):
        user = request.user
        card_list = StripeCardClient.list_cards(self, user)
        return Response(card_list, status=status.HTTP_200_OK)

    def delete(self, request):
        card_delete = StripeCardClient.delete_card(self, request)
        return Response(card_delete, status=status.HTTP_200_OK)
