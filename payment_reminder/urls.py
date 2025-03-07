from django.urls import path
from . import views

app_name = "payment_reminder"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("client/", views.ClientsView.as_view(), name="clients"),
    path("client/<int:pk>/", views.DetailView.as_view(), name="client_detail"),
    path("client/create/", views.create_client, name="create_client"),
]