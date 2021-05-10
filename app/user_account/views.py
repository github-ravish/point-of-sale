from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text

from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    TemplateView,
    View,
)

from user_account.forms import (
    UserAccountCreationForm,
    UserAccountLoginForm,
    UserAccountChangePasswordForm,
    UserAccountPasswordResetInitiateForm,
    UserAccountPasswordResetForm,
)


from user_account.models import UserAccount
from user_account.tokens import account_activation_token


class UserAccountCreateView(CreateView):
    form_class = UserAccountCreationForm
    template_name = 'user_account/signup.html'
    success_url = reverse_lazy('user_account:activate')

    def get_form_kwargs(self):
        kwargs = super(UserAccountCreateView, self).get_form_kwargs()
        referral_code = self.kwargs.get("referral_code", None)
        kwargs.update({'referral_code': referral_code})
        return kwargs


class UserAccountActivateInitiateView(TemplateView):
    template_name = 'user_account/activate/activate.html'


class UserAccountActivateConfirmView(View):
    success_url = 'user_account/activate/activate_confirm.html'
    validlink = False

    def get(self, request, *args, **kwargs):

        context = dict()
        user = UserAccount.objects.get_object_by_uidb64(kwargs.get('uidb64'))
        if user and account_activation_token.check_token(user, kwargs.get('token')) and not user.is_active:
            user.is_active = True
            user.save()
            validlink = True
        context['validlink'] = validlink
        return render(request, self.success_url, context=context)


class UserAccountLoginView(LoginView):
    authentication_form = UserAccountLoginForm
    template_name = 'user_account/login.html'
    redirect_authenticated_user = True


class UserAccountDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user_account/profile/home.html'
    queryset = UserAccount.objects.all()
    context_object_name = 'user_detail'

    def get_object(self, queryset=None):
        return self.request.user


class UserAccountChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserAccountChangePasswordForm
    template_name = 'user_account/password/change_password.html'
    success_url = reverse_lazy('account:detail_home')


class UserAccountResetPasswordInitiateView(PasswordResetView):
    template_name = 'user_account/password/reset_password_initiate.html'
    email_template_name = 'utils/password_reset_email.html'
    form_class = UserAccountPasswordResetInitiateForm
    success_url = reverse_lazy('user_account:reset_password_initiate_confirm')


class UserAccountResetPasswordInitiateConfirmView(PasswordResetDoneView):
    template_name = 'user_account/password/reset_password_initiate_confirm.html'


class UserAccountResetPasswordView(PasswordResetConfirmView):
    template_name = 'user_account/password/reset_password.html'
    form_class = UserAccountPasswordResetForm
    success_url = reverse_lazy('user_account:login')
