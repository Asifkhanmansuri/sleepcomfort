from django.shortcuts import render
from productCategory.models import Facility, Testmonial, Client_Rating, Product_Card

# Create your views here.
def bedding(request):
    facility= Facility.objects.all()
    testimonial=Testmonial.objects.filter(product_category__name = "Bedding")
    clientRating= Client_Rating.objects.filter(product_category__name='Bedding')
    card= Product_Card.objects.filter(productCategory__name='Bedding')
    return render(request, 'Bedding/bedding.html', {'facility':facility,'cards':card, 'testimonial':testimonial, "clientRating":clientRating})
    