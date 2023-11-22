from django.shortcuts import render

from .models import Mattress_Product
from productCategory.models import  Facility, Testmonial, Client_Rating, Product_Card, Size 

# Create your views here.

def mattress(request):
   
            
   
    testimonial=Testmonial.objects.filter(product_category__name = "Mattress")
    clientRating= Client_Rating.objects.filter(product_category__name='Mattress')
    size= Size.objects.all()
    facility= Facility.objects.all()
    card= Product_Card.objects.filter(productCategory__name='Mattress')
    return render(request, 'Mattress/mattress.html',{'testimonial': testimonial,  'size':size, 'facility':facility, 'clientRating':clientRating, 'cards':card})