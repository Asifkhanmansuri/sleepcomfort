from django.urls import path
from .import views
urlpatterns = [
    path('babyrange', views.babyRange, name='babyRange')
]
