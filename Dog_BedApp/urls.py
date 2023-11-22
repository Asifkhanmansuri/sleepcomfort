from django.urls import path
from .import views
urlpatterns = [
   path("dogBed", views.dogBed, name='dogBed') 
]
