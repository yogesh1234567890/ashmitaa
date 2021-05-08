from django.shortcuts import render, redirect, HttpResponse
from .models import *
from bookblog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.forms import ContactForm

# Create your views here.
#main homepage 
def home(request):
    allpost = Post.objects.all()
    context = {'allpost': allpost}
    return render(request, 'home/home.html', context)

#Contact form for the user
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

#about author
def about(request):
    return render(request, 'home/about.html')

#Search handling
def search(request):
    query = request.GET['query']
    alltitle = Post.objects.filter(blog_title__icontains=query)
    allcontent = Post.objects.filter(content__icontains=query)
    allpost = alltitle.union(allcontent)

    context = {'allpost': allpost, 'query': query}
    return render(request, 'home/search.html', context) 

#Handling signup
def handleSignup(request):
    if request.method =="POST":
        #then get all the datas
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for the inputs
        #username must be greater than 5 letters or numbers
        if len(username)<5:
            messages.error(request, " Your user name must not be under 5 characters")
            return redirect('home')

        #username must contain alphabets and numeric values only
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        
        #checking password1 and password2
        if (pass1!= pass2):
             messages.error(request, "Passwords do not match")
             return redirect('home')

        #creating user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your blog account has been successfully created")

        return redirect('home')
    else:
        return HttpResponse("404 - Not Found")


def handlelogin(request):
    if request.method =="POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
        else:
            messages.error(request, 'Invalid Credentials, Please Try Again')
    
    return redirect('home')

def handlelogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')