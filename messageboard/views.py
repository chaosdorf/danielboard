from django.shortcuts import render, redirect
from .models import Post

# Create your views here.


def overview(request):
    context = {
        "posts": Post.objects.all().order_by("-sent")
    }
    return render(request, "messageboard/overview.html.j2", context)


def submit(request):
    title = request.POST["title"]
    content = request.POST["content"]
    post = Post(title=title, content=content)
    post.save()
    return redirect("overview")
