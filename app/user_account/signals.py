from allauth.account.signals import user_signed_up
from django.dispatch import Signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from user_account.models import UserAccount
from user_account.tokens import account_activation_token

user_created = Signal(providing_args=["user", "referral_code"])


@receiver(user_signed_up)
def confirm_user_account(request, user, **kwargs):
    if not user.is_active:
        user.is_active = True
        user.save()


@receiver(post_save, sender=UserAccount)
def send_user_activation_email(sender, instance, created, **kwargs):
    if created:
        uidb64 = urlsafe_base64_encode(force_bytes(instance.id))
        token = account_activation_token.make_token(instance)
        # Send activation email
