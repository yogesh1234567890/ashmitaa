from django.db import models
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, blank=True, null= True)

    def __str__(self):
        return self.user.username
