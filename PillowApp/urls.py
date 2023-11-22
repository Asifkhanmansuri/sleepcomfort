from django.urls import path
from .import views
urlpatterns = [
    path('pillow', views.pillow, name='pillow')
]
