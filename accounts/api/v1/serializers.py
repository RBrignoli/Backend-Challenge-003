"""
API V1: Accounts Serializers
"""
###
# Libraries
###
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
        fields = ('height', 'weight', 'date_of_birth', 'gender', 'address', 'mobile_country_code', 'mobile_phone_number', 'strip_id')



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
    address = serializers.DateField(
        allow_null=True,
    )

    mobile_country_code = serializers.IntegerField(
        max_length=8,
        allow_null=True,
    )
    mobile_phone_number = serializers.IntegerField(
        max_length=30,
        allow_null=True,
    )
    strip_id = serializers.CharField(
        max_length=255,
        allow_null=True,
    )
