from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.

def bloghome(request):
    allpost = Post.objects.all()
    context = {'allpost': allpost}
    return render(request, 'bookblog/bloghome.html', context)

def blogpost(request, id):
    print(id,'--------------')
    post = Post.objects.get(pk = id)
    context = {'post': post}
    return render(request, 'bookblog/blogpost.html', context)