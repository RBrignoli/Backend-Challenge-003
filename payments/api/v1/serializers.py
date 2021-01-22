"""
API V1: Payments Serializers
"""
###
# Libraries
###
from rest_framework import serializers


###
# Serializers
###
class CreateCardSerializer(serializers.Serializer):
    number = serializers.CharField(
        required=True,
        max_length=16,
    )
    exp_month = serializers.CharField(
        required=True,
        max_length=2,
    )
    exp_year = serializers.CharField(
        required=True,
        max_length=4,
    )
    cvc = serializers.CharField(
        required=True,
        max_length=3,
    )


