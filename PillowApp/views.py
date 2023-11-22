from django.shortcuts import render, redirect
from productCategory.models import Testmonial, Client_Rating, Facility,Product_Card

# Create your views here.
def pillow(request):
    facility= Facility.objects.all()
    testimonial=Testmonial.objects.filter(product_category__name = "Pillow")
    clientRating= Client_Rating.objects.filter(product_category__name='Pillow')
    card= Product_Card.objects.filter(productCategory__name='Pillow')
    return render(request,'Pillow/pillow.html', {'facility':facility, 'testimonial':testimonial, "clientRating":clientRating, 'cards':card})