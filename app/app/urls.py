"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user_account.urls', namespace='user_account')),
    path('all_auth/', include('allauth.urls')),

]


urlpatterns += i18n_patterns(
    path('', include('static_page.urls', namespace='static_page')),

    path('shop/', include('shop.urls', namespace='shop')),
    path('product/', include('product.urls', namespace='product')),
    path('order/', include('order.urls', namespace='order')),
    path('transaction/', include('transaction.urls', namespace='transaction')),
)

urlpatterns += i18n_patterns(
    path('api/product/', include('product.api.urls', namespace='product_api')),
    path('api/order/', include('order.api.urls', namespace='order_api')),
)
