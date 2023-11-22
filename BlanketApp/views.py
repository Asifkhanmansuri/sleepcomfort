from django.shortcuts import render
from productCategory .models import Facility, Testmonial, Client_Rating, Product_Card

# Create your views here.
def blanket(request):
    testimonial=Testmonial.objects.filter(product_category__name = "Blanket")

    facility= Facility.objects.all()
    testimonial=Testmonial.objects.filter(product_category__name = "Blanket")
    clientRating= Client_Rating.objects.filter(product_category__name='Blanket')
    card= Product_Card.objects.filter(productCategory__name='Blanket')
    return render(request, 'Blanket/blanket.html', {'facility':facility,'cards':card, 'testimonial': testimonial, 'clientRating':clientRating})