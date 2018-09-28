from django.shortcuts import render
from .models import Post

def index(request):
    post_filter = Post.objects.all().order_by("post_time")
    return render(request, "vision/index.html", {"post_filter":post_filter})
