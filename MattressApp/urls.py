from django.urls import path
from .import views
urlpatterns = [
    path("", views.mattress, name='mattress')
]
