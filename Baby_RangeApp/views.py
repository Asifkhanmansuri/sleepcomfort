from django.shortcuts import render
from productCategory.models import Facility, Testmonial, Client_Rating, Product_Card

# Create your views here.
def babyRange(request):
    facility= Facility.objects.all()
    testimonial=Testmonial.objects.filter(product_category__name = "Baby Range")
    clientRating= Client_Rating.objects.filter(product_category__name='Baby Range')
    card= Product_Card.objects.filter(productCategory__name='Baby Range')
    return render(request, 'Baby Range/babyRange.html', {'facility':facility, 'testimonial':testimonial, "clientRating":clientRating, "cards":card})
    