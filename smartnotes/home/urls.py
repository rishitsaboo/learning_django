from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home), # URL for the home page
    path('authorized', views.authorized), # URL for the authorized page
]