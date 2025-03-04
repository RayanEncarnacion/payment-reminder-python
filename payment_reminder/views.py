from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world! You're at the payment reminder index.")

def login(request):
    return render(request, "payment_reminder/login.html")
