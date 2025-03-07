from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms.client import CreateClient
from .models import Client, User
from django.urls import reverse
from django.views import generic

BASE_TEMPLATES_PATH = "payment_reminder/"
CLIENT_TEMPLATES_PATH = BASE_TEMPLATES_PATH + "client/"

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

def login(request):
    return render(request, BASE_TEMPLATES_PATH + "login.html")

def create_client(request):
    return render(request, CLIENT_TEMPLATES_PATH + "create.html")

def store_client(request):
    form = CreateClient(request.POST)
    
    if form.is_valid():
        client = Client(name=request.POST["name"], email=request.POST["email"], createdBy=User.objects.first())
        client.save()
        
        return HttpResponseRedirect(reverse("payment_reminder:clients"))
    else:
        return render(
            request,
            CLIENT_TEMPLATES_PATH + "create.html",
            {
                "errors": form.errors,
            },
        )
