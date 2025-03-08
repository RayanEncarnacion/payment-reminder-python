from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "payment_reminder"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="payment_reminder/login.html", next_page="/client/"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
    path("client/", views.ClientsView.as_view(), name="clients"),
    path("client/<int:pk>/", views.DetailView.as_view(), name="client_detail"),
    path("client/create/", views.create_client, name="create_client"),
    path("project/create/", views.create_project, name="create_project"),
]