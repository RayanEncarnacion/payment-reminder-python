from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import CreateClient, CreateProject
from .models import Client, Project

BASE_TEMPLATES_PATH = "payment_reminder/"
CLIENT_TEMPLATES_PATH = BASE_TEMPLATES_PATH + "client/"
PROJECT_TEMPLATES_PATH = BASE_TEMPLATES_PATH + "project/"

class ClientsView(generic.ListView):
    template_name = CLIENT_TEMPLATES_PATH + "index.html"

    def get_queryset(self):
        return Client.objects.filter(deleted__exact=False)
    
class ProjectsView(generic.ListView):
    template_name = PROJECT_TEMPLATES_PATH + "index.html"

    def get_queryset(self):
        return (
                Project.objects
                       .select_related("client")
                       .filter(deleted__exact=False)
                       .order_by("-createdAt")
               )
    
def index(request):
   return render(request, BASE_TEMPLATES_PATH + "index.html")

def delete(request, model, id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    model.objects.get(id=id).delete()

@login_required
def CreateClientView(request):
    if request.method == "POST":
        form = CreateClient(request.POST)
        
        if not form.is_valid():
            return render(request, CLIENT_TEMPLATES_PATH + "create.html", { "errors": form.errors })
        
        client = Client(name=request.POST["name"], email=request.POST["email"], createdBy=request.user)
        client.save()
        return HttpResponseRedirect(reverse("payment_reminder:clients"))
    
    else:
        return render(request, CLIENT_TEMPLATES_PATH + "create.html", { "form": CreateClient() })

@login_required
def DeleteClient(request, pk):
    delete(request, Client, pk)
    return HttpResponseRedirect(reverse("payment_reminder:clients"))

@login_required
def CreateProjectView(request):
    
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
    
@login_required
def DeleteProject(request, pk):
    delete(request, Project, pk)
    return HttpResponseRedirect(reverse("payment_reminder:projects"))


