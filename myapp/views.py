from django.shortcuts import render
from .models import Post  # Make sure to import your model

#from django.http import HttpResponse 

def home(request):
    return render(request, "home.html")
    
def post_list(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'posts.html', {'posts': posts})  # Pass posts to the template