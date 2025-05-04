from django.urls import path
from . import views


urlpatterns = [
    path('home', views.HomeView.as_view()), # URL for the home page
    path('authorized', views.AuthorizedView.as_view()), # URL for the authorized page
]