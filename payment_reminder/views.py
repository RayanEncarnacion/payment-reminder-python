from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateClient, CreateProject
from .models import Client, Project

BASE_TEMPLATES_PATH = "payment_reminder/"
CLIENT_TEMPLATES_PATH = BASE_TEMPLATES_PATH + "client/"
PROJECT_TEMPLATES_PATH = BASE_TEMPLATES_PATH + "project/"

@login_required  
def index(request):
   return render(request, BASE_TEMPLATES_PATH + "index.html")
class ClientsView(LoginRequiredMixin, generic.ListView):
    template_name = CLIENT_TEMPLATES_PATH + "index.html"

    def get_queryset(self):
        return (Client.objects.filter(deleted__exact=False)
                              .order_by("-createdAt"))

class ClientDetails(LoginRequiredMixin, generic.DetailView):
    template_name = CLIENT_TEMPLATES_PATH + "detail.html"
    model = Client
    
class ProjectDetails(LoginRequiredMixin, generic.DetailView):
    template_name = PROJECT_TEMPLATES_PATH + "detail.html"
    
    def get_queryset(self):
        return Project.objects.filter(id = self.kwargs[self.pk_url_kwarg])

class ProjectsView(LoginRequiredMixin, generic.ListView):
    template_name = PROJECT_TEMPLATES_PATH + "index.html"

    def get_queryset(self):
        return (Project.objects.select_related("client")
                               .filter(deleted__exact=False)
                               .order_by("-createdAt"))
        
@login_required  
def clientProjectsView(request, pk):
    projects = (Project.objects.filter(deleted__exact=False, client_id=pk)
                               .order_by("-createdAt"))
    
    return render(request, CLIENT_TEMPLATES_PATH + "projects.html", { "projects": projects, "pk": pk })

@login_required
def createClientView(request):
    if request.method == "POST":
        form = CreateClient(request.POST)
        
        if not form.is_valid():
            return render(request, CLIENT_TEMPLATES_PATH + "create.html", { "errors": form.errors })
        
        Client(
            name=request.POST["name"], 
            email=request.POST["email"], 
            createdBy=request.user
        ).save()
        
        return HttpResponseRedirect(reverse("payment_reminder:clients"))
    
    else:
        return render(request, CLIENT_TEMPLATES_PATH + "create.html", { "form": CreateClient() })

@require_http_methods(["POST"])
@login_required
def deleteClient(_, pk):
    Client.objects.get(pk).delete()
    return HttpResponseRedirect(reverse("payment_reminder:clients"))

@login_required
def createProjectView(request):
    
    if request.method == "POST":
        form = CreateProject(request.POST)
        
        if not form.is_valid():
            return render(request, PROJECT_TEMPLATES_PATH + "create.html", { "form": form })
        
        Project(
            name=request.POST["name"], 
            amount=request.POST["amount"], 
            client=form.cleaned_data["client"],
            createdBy=request.user
        ).save()
        
        return HttpResponseRedirect(reverse("payment_reminder:projects"))
    else:
        return render(request, PROJECT_TEMPLATES_PATH + "create.html", { "form": CreateProject() })

@require_http_methods(["POST"]) 
@login_required
def deleteProject(request, pk):
    Project.objects.get(pk).delete()
    return HttpResponseRedirect(reverse("payment_reminder:projects"))


