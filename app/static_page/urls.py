from django.urls import path

from .views import (
	HomeView
)

app_name = 'static_page'

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
]