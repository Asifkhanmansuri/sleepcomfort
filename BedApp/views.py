from django.shortcuts import render
from productCategory.models import Facility, Testmonial, Client_Rating,Product_Card

# Create your views here.
def bed(request):
    facility= Facility.objects.all()
    testimonial=Testmonial.objects.filter(product_category__name = "Bed")
    clientRating= Client_Rating.objects.filter(product_category__name='Bed')
    card= Product_Card.objects.filter(productCategory__name='Bed')
    return render(request, 'Bed/bed.html', {'facility':facility, 'testimonial':testimonial, "clientRating":clientRating, 'cards':card})
    