from django.urls import path
from django.contrib.auth import views as auth_views

from user_account.views import (
    UserAccountCreateView,
    UserAccountLoginView,
    UserAccountActivateInitiateView,
    UserAccountActivateConfirmView,
    UserAccountDetailView,
    UserAccountChangePasswordView,
    UserAccountResetPasswordInitiateView,
    UserAccountResetPasswordInitiateConfirmView,
    UserAccountResetPasswordView
)

app_name = 'account'

urlpatterns = [
    path('signup/<str:referral_code>/', UserAccountCreateView.as_view(),
         name='create_with_referral'),
    path('signup/', UserAccountCreateView.as_view(), name='create'),

    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# For activation routes
urlpatterns += [
    path('activate/<uidb64>/<str:token>/', UserAccountActivateConfirmView.as_view(),
         name='activate_confirm'),
    path('activate/', UserAccountActivateInitiateView.as_view(),
         name='activate'),
]

# For profile routes
urlpatterns += [
    path('profile/', UserAccountDetailView.as_view(), name='detail_home'),
]

# For password

urlpatterns += [
    path('password/change/', UserAccountChangePasswordView.as_view(),
         name='change_password'),
    path('password/reset/initiate/', UserAccountResetPasswordInitiateView.as_view(),
         name='reset_password_initiate'),
    path('password/reset/initiate/confirm', UserAccountResetPasswordInitiateConfirmView.as_view(),
         name='reset_password_initiate_confirm'),
    path('password/reset/<uidb64>/<token>/', UserAccountResetPasswordView.as_view(),
         name='reset_password'),
]
