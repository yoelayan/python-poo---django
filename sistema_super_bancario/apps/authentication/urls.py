from .views import (
    CustomLoginView,
    CustomLogoutView
)
from django.urls import path
urlpatterns = [
    path("login", CustomLoginView.as_view(), name="login"),
    path("logout", CustomLogoutView.as_view(), name="logout"),
]
