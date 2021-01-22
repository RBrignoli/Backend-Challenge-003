"""
API V1: Payments Views
"""
###
# Libraries
###
from rest_framework import viewsets, permissions, status
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





class CardViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateCardSerializer








