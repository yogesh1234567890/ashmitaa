from django.db import models

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
