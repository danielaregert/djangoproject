from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings  # ✅ Import settings
from django.conf.urls.static import static  # ✅ Import static

urlpatterns = [
    path('posts/', views.post_list, name='posts'),  # Now views.post_list is recognized
    path('', views.home, name='home'),  # views.home should also be defined in views.py
] 