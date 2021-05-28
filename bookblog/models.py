from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Post(models.Model):
    blog_title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    about_author = models.TextField()
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateField(blank=True)

    def __str__(self):
        return self.blog_title + ' blog by ' + self.author


class BlogComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:10] + "..." + self.user.username


# class LoggedInUser(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=32, blank=True, null= True)

#     def __str__(self):
#         return self.user.username

