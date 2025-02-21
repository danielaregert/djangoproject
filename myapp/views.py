from django.shortcuts import render, redirect
from .models import Post  # Make sure to import your model
from django.core.mail import send_mail
from .forms import ContactForm

#from django.http import HttpResponse 

def home(request):
    return render(request, "home.html")
    
def post_list(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'posts.html', {'posts': posts})  # Pass posts to the template


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"Mi website: Nuevo mensaje de {name}"
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(subject, full_message, "danielaregert@gmail.com", ["danielaregert@gmail.com"])

            return redirect("success")  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

def success_view(request):
    return render(request, "success.html")