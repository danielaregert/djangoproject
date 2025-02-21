from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static  
from . import views  
from .views import contact_view
from .views import success_view  

urlpatterns = [
    path('posts/', views.post_list, name='posts'),  # Now views.post_list is recognized
    path('', views.home, name='home'),  # views.home should also be defined in views.py
    path("contact/", contact_view, name="contact"),
    path("success/", success_view, name="success"), 
] 