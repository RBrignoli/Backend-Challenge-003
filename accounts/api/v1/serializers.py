"""
API V1: Accounts Serializers
"""
###
# Libraries
###
from allauth.account.utils import setup_user_email
from django.contrib.auth.models import User
from rest_auth.models import TokenModel
from rest_auth.serializers import (
    UserDetailsSerializer as BaseUserDetailsSerializer,
    PasswordResetSerializer as BasePasswordResetSerializer,
)
from rest_framework import serializers
from rest_framework.validators import ValidationError

from accounts.forms import (
    CustomResetPasswordForm,
)
from accounts.models import User, GENDER_CHOICES

from rest_auth.registration.serializers import RegisterSerializer as BaseRegisterSerializer

###
# Serializers
###
class UserTokenSerializer(serializers.ModelSerializer):
    user = BaseUserDetailsSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user',)


class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        user = self.context['request'].user

        if user.email == email:
            raise ValidationError('Cannot change to the same email.')

        if User.objects.exclude(id=user.id).filter(email=email).exists():
            raise ValidationError('Another account already exists with this email.')

        return email


class PasswordResetSerializer(BasePasswordResetSerializer):
    password_reset_form_class = CustomResetPasswordForm

    def get_email_options(self):
        return {
            'subject_template_name': 'account/password_reset_subject.txt',
            'email_template_name': 'account/password_reset_message.txt',
            'html_email_template_name': 'account/password_reset_message.html',
        }


class UserProfileWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name','height', 'weight', 'date_of_birth', 'gender', 'address', 'mobile_country_code', 'mobile_phone_number', 'strip_id')



class RegisterSerializer(BaseRegisterSerializer):

    name = serializers.CharField(
        write_only=True,
        max_length=64,
        required=True,
        allow_blank=False,
    )

    height = serializers.CharField(
        max_length=255,
        allow_null=True,
    )
    weight = serializers.CharField(
        max_length=255,
        allow_null=True,
    )
    date_of_birth = serializers.DateField(
        allow_null=True,
    )
    gender = serializers.ChoiceField(
        choices=GENDER_CHOICES,

    )
    address = serializers.CharField(
        max_length=100,
        allow_null=True,
    )

    mobile_country_code = serializers.CharField(
        max_length=8,
        allow_null=True,
    )
    mobile_phone_number = serializers.CharField(
        max_length=30,
        allow_null=True,
    )
    stripe_id = serializers.CharField(
        max_length=255,
        allow_null=True,
        allow_blank=True,
        required=False,
    )

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'height': self.validated_data.get('height', ''),
            'weight': self.validated_data.get('weight', ''),
            'date_of_birth': self.validated_data.get('date_of_birth', ''),
            'gender': self.validated_data.get('gender', ''),
            'address': self.validated_data.get('address', ''),
            'mobile_country_code': self.validated_data.get('mobile_country_code', ''),
            'mobile_phone_number': self.validated_data.get('mobile_phone_number', ''),
            'stripe_id': self.validated_data.get('stripe_id', ''),


        }

    def custom_signup(self, request, user):
        cleaned_data = self.get_cleaned_data()
        user.email = cleaned_data().get('email')
        user.name = cleaned_data().get('name')
        user.height = cleaned_data().get('height')
        user.weight = cleaned_data().get('weight')
        user.date_of_birth = cleaned_data().get('date_of_birth')
        user.gender = cleaned_data().get('gender')
        user.address = cleaned_data().get('address')
        user.mobile_country_code = cleaned_data().get('mobile_country_code')
        user.mobile_phone_number = cleaned_data().get('mobile_phone_number')
        user.stripe_id = cleaned_data().get('stripe_id')

        user.save()



