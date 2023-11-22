from django.urls import path
from  .import views
urlpatterns = [
    path("", views.home, name="home"),
    path('contact', views.contact, name='contact'),
    path("productDetail/<int:pk>", views.productDetail, name='productDetail'),
    path('login', views.login, name='login'),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name='register'),
    path("cart", views.cart, name="cart"),
    path("addCart", views.addCart, name="addCart"),
    path("searchQuery", views.searchQuery, name="searchQuery"),
    path("buyNow/<int:pk>", views.buyNow, name="buynow"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("edit/<int:pk>", views.edit, name="edit" )
]

