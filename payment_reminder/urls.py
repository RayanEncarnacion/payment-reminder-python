from django.urls import path
from . import views

app_name = "payment_reminder"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("client/", views.clients, name="clients"),
    path("client/create/", views.create_client, name="create_client"),
    path("client/store/", views.store_client, name="store_client"),
]