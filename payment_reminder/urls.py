from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic

from . import views
from .models import Client, Project

app_name = "payment_reminder"

urlpatterns = [
    path("", views.index, name="index"),
    
    # Auth views
    path("login/", auth_views.LoginView.as_view(template_name="payment_reminder/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
    
    # Client views
    path("client/", views.ClientsView.as_view(), name="clients"),
    path("client/create/", views.create_client, name="create_client"),
    path("client/<int:pk>/", 
         generic.DetailView.as_view(template_name="payment_reminder/client/detail.html", model=Client), 
         name="client_detail"),
    
    # Project views
    path("project/", views.ProjectsView.as_view(), name="projects"),
    path("project/create/", views.create_project, name="create_project"),
    path("project/<int:pk>/", 
         generic.DetailView.as_view(template_name="payment_reminder/project/detail.html", model=Project), 
         name="project_detail"),
]
