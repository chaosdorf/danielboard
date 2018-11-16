from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def overview(request):
    context = {
        "posts": Post.objects.all().order_by("-sent")
    }
    return HttpResponse(context["posts"])


def submit(request):
    return HttpResponse("This creates a new message.")
