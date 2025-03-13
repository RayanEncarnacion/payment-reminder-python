from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic

from . import views
from .models import Project

app_name = "payment_reminder"

urlpatterns = [
    path("", views.index, name="index"),
    
    # Auth views
    path("login/", auth_views.LoginView.as_view(template_name="payment_reminder/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
    
    # Client views
    path("client/", views.ClientsView.as_view(), name="clients"),
    path("client/create/", views.createClientView, name="client_create"),
    path("client/<int:pk>/", views.ClientDetails.as_view(), name="client_details"),
    path("client/<int:pk>/projects", 
         views.clientProjectsView, 
         name="client_projects"),
      path("client/<int:pk>/delete/", 
         views.deleteClient, 
         name="client_delete"),
    
    # Project views
    path("project/", views.ProjectsView.as_view(), name="projects"),
    path("project/create/", views.createProjectView, name="project_create"),
    path("project/<int:pk>/", views.ProjectDetails.as_view(), name="project_details"),
    path("project/<int:pk>/delete/", 
         views.deleteProject, 
         name="project_delete"),
]
