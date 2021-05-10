import uuid
from django.utils.encoding import force_bytes
from django.core.signing import Signer
from django.utils.http import urlsafe_base64_encode
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class UserProfile(models.Model):
    """ User model for the project """
    OTP_CATEGORY = [
        ('MV', 'Mobile Verification')
    ]
    user_account = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_profile"
    )
    referred_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    otp_category = models.CharField(
        max_length=5,
        choices=OTP_CATEGORY,
        default="MV"
    )
    otp = models.IntegerField(null=True)

    def get_referral_code(self):
        return urlsafe_base64_encode(force_bytes(self.user_account.id))
