from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def overview(request):
    return HttpResponse("Here be messages.")


def submit(request):
    return HttpResponse("This creates a new message.")
