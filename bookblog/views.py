from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from bookblog.templatetags import extras
from django.contrib.auth.models import User

# Create your views here.

def bloghome(request):
    allpost = Post.objects.all()
    context = {'allpost': allpost}
    return render(request, 'bookblog/bloghome.html', context)

def blogpost(request, id):
    post = Post.objects.get(pk=id)
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replydict = {}

    for reply in replies:
        if reply.parent.pk not in replydict.keys():
            replydict[reply.parent.pk] = [reply]
        else:
            replydict[reply.parent.pk].append(reply)
    context = {'post': post, 'comments': comments, 'user': request.user, 'replydict': replydict}

    return render(request, 'bookblog/blogpost.html', context)

def postComment(request):                                                        
    if request.method =="POST":
        comment = request.POST.get('comment')
        user = request.user
        post = Post.objects.get(pk=request.POST['post_id'])
        parentId = request.POST.get("parentId")

        if parentId =="":
            comment = BlogComment(comment=comment, user=user, post= post)
            comment.save()
            messages.success(request, 'your comment has been posted')

        else:
            parent=BlogComment.objects.get(pk=parentId)
            comment = BlogComment(comment=comment, user=user, post= post, parent=parent)
            comment.save()
            messages.success(request, 'your reply has been posted')

    return redirect(f'/blog/blogpost/{post.id}')