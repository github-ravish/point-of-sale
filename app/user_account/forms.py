import re
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Column, Row
from crispy_forms.bootstrap import AppendedText, PrependedText

from user_account.models import UserAccount
from user_account.signals import user_created


class UserAccountCreationForm(UserCreationForm):

    first_name = forms.CharField(
        label=_("First Name"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }),
        max_length=50, required=True
    )
    last_name = forms.CharField(
        label=_("Last Name"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }),
        max_length=50, required=True
    )
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
        max_length=255, required=True
    )
    phone = forms.CharField(
        label=_("Phone"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mobile Number'
        }),
        max_length=15, required=True
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'toggle-password-type',
                'placeholder': 'Enter Password'
            }),
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-Enter Password'
        }),
    )

    class Meta:
        model = UserAccount
        fields = (
            'first_name', 'last_name', 'email', 'phone', 'password1', 'password2',
        )

    def __init__(self, referral_code=None, *args, **kwargs):
        super(UserAccountCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', wrapper_class="form-group com-sm-6"),
                Column('last_name', wrapper_class="form-group com-sm-6"),
                css_class="form-row"
            ),
            'email',
            'phone',
            Row(
                Column(Field(AppendedText('password1', '<span onclick="passwordTypeToggle()" class="material-icons material-icons-outlined password-toggle">visibility_off</span>')),
                       wrapper_class="form-group com-sm-6"),
                Column('password2', wrapper_class="form-group com-sm-6"),
                css_class="form-row"
            ),
        )
        self.referral_code = referral_code

    def clean_first_name(self):

        first_name = self.cleaned_data.get("first_name")
        if not re.search("^[A-Za-z]+$", first_name):
            raise ValidationError('First name is invalid.')
        return first_name

    def clean_last_name(self):

        last_name = self.cleaned_data.get("last_name")
        if not re.search("^[A-Za-z]+$", last_name):
            raise ValidationError(
                'Last name is invalid.')
        return last_name

    def clean_email(self):

        email = self.cleaned_data.get("email")
        if not re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",
                         email):
            raise ValidationError('Email is invalid.')
        if UserAccount.objects.filter(email=email).count() > 0:
            raise ValidationError('Email is invalid.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        re_matches = re.search(
            "^((\+){0,1}\d{2,3}){1}[ -]{0,1}([1-9]{1}[0-9]{9})$", phone)
        if not re_matches:
            raise ValidationError(
                'Phone no invalid. Format: +91 9999999999')
        return re_matches.group(1) + " " + re_matches.group(3)

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not re.search(
                "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@!#$%&*()_+-= ]{8,}$",
                password1
        ):
            raise ValidationError(
                'Password should have 8 to 15 characters which contain only characters, numeric digits, underscore and first character must be a letter', code='signup'
            )
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserAccountCreationForm, self).save(commit=False)
        if commit:
            user.save()
        user_created.send(self.__class__, user=user,
                          referral_code=self.referral_code)
        return user


class UserAccountLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
        max_length=255, required=True
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'toggle-password-type',
                'placeholder': 'Enter Password'
            }),
    )

    class Meta:
        model = UserAccount
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'username',
            Field(AppendedText('password',
                  '<span onclick="passwordTypeToggle()" class="material-icons material-icons-outlined password-toggle">visibility_off</span>'))
        )


class UserAccountChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Old Password'
            }),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'toggle-password-type',
                'placeholder': 'New Password'
            }),
    )
    new_password2 = forms.CharField(
        label=_("Confirm new password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }),
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'old_password',
            Field(AppendedText('new_password1',
                  '<span onclick="passwordTypeToggle()" class="material-icons material-icons-outlined password-toggle">visibility_off</span>')),
            'new_password2',
        )

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get("new_password1")
        if not re.search(
                "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@!#$%&*()_+-= ]{8,}$",
                new_password1
        ):
            raise ValidationError(
                'Password should have 8 to 15 characters which contain only characters, numeric digits, underscore and first character must be a letter', code='signup'
            )
        return new_password1


class UserAccountPasswordResetInitiateForm(PasswordResetForm):

    email = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        }),
        max_length=255,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'email',
        )

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        pass

    def clean_email(self):

        email = self.cleaned_data.get("email")
        if not re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",
                         email):
            raise ValidationError('Email is invalid.')

        if not UserAccount.objects.get_object_or_none(email__iexact=email, is_active=True):
            raise ValidationError('Email is invalid.')

        return email


class UserAccountPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'toggle-password-type',
                'placeholder': 'New Password'
            }),
    )
    new_password2 = forms.CharField(
        label=_("Confirm new password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm New Password'
            }),
    )

    class Meta:
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field(AppendedText('new_password1',
                  '<span onclick="passwordTypeToggle()" class="material-icons material-icons-outlined password-toggle">visibility_off</span>')),
            'new_password2',
        )

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get("new_password1")
        if not re.search(
                "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@!#$%&*()_+-= ]{8,}$",
                new_password1
        ):
            raise ValidationError(
                'Password should have 8 to 15 characters which contain only characters, numeric digits, underscore and first character must be a letter', code='signup'
            )
        return new_password1
