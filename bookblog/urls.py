from django.urls import path 
from . import views
urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('', views.bloghome, name='bloghome'),
    path('blogpost/<int:id>/', views.blogpost, name='blogpost'),
    #API to post comment
    
]