from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateClient, CreateProject
from .models import Client, Project
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

BASE_TEMPLATES_PATH = "payment_reminder/"
CLIENT_TEMPLATES_PATH = BASE_TEMPLATES_PATH + "client/"
PROJECT_TEMPLATES_PATH = BASE_TEMPLATES_PATH + "project/"

class ClientsView(generic.ListView):
    template_name = CLIENT_TEMPLATES_PATH + "index.html"
    # To rename the passed variables names -> context_object_name = "clients"
    # By default its "<MODEL>_list" (client_list)

    def get_queryset(self):
        return Client.objects.filter(deleted__exact=False)
    
class DetailView(generic.DetailView):
    model = Client
    template_name = CLIENT_TEMPLATES_PATH + "detail.html"
    
def index(request):
    return HttpResponse("Hello, world! You're at the payment reminder index.")

@login_required
def create_client(request):
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
def create_project(request):
    
    if request.method == "POST":
        form = CreateProject(request.POST)
        
        if not form.is_valid():
            return render(request, PROJECT_TEMPLATES_PATH + "create.html", { "form": form.errors })
        
        client = get_object_or_404(Client, pk=request.POST["client"])
        # Add try catch logic
        project = Project(name=request.POST["name"], 
                            amount=request.POST["amount"], 
                            client=client,
                            createdBy=request.user)
        project.save()
        return HttpResponseRedirect(reverse("payment_reminder:create_project"))
    else:
        return render(request, PROJECT_TEMPLATES_PATH + "create.html", { "form": CreateProject() })


