from django.shortcuts import render
from productCategory.models import Testmonial, Facility, Client_Rating, Product_Card

# Create your views here.
def dogBed(request):
    facility= Facility.objects.all()
    testimonial=Testmonial.objects.filter(product_category__name = "Dog Bed")
    clientRating= Client_Rating.objects.filter(product_category__name='Dog Bed')
    card= Product_Card.objects.filter(productCategory__name='Dog Bed')
    return render(request, 'Dog Bed/dogBed.html', {'facility':facility, "cards":card ,'testimonial':testimonial, "clientRating":clientRating})
    