from django.shortcuts import render, redirect, HttpResponse
from .models import *
from bookblog.models import Post
from home.forms import ContactForm

# Create your views here.

def home(request):
    allpost = Post.objects.all()
    context = {'allpost': allpost}
    return render(request, 'home/home.html', context)

def contact(request):
    if request.method =="GET":
        contactform = ContactForm()
        context = {'contactform': contactform}
        return render(request, 'home/contact.html', context)
    
    if request.method =="POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
        
        print(contactform)
        return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']
    allpost = Post.objects.filter(blog_title__icontains=query)
    context = {'allpost': allpost}
    return render(request, 'home/search.html', context) 

