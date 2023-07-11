from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect("create")
    return render(request, "html/post.html")