from django.urls import path
from .import views
urlpatterns = [
    path('bedding', views.bedding, name='bedding')
]
