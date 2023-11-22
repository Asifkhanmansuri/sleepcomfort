from django.contrib import admin
from .models import Product_Category, Product_Card, Testmonial, Facility,\
    Client_Rating, Header_ProductButton, Size, Cart, Order, User_Detail

# Register your models here.
admin.site.register(Product_Category)

admin.site.register(Product_Card)

admin.site.register(Testmonial)
admin.site.register(Facility)
admin.site.register(Client_Rating)

admin.site.register(Header_ProductButton)
admin.site.register(Size)


class AdminCart(admin.ModelAdmin):
    
    list_display = ["id","product","productCategory","user"]


admin.site.register(Cart, AdminCart)

class AdminOrder(admin.ModelAdmin):
    list_display= ["id","Product", "Product_category", "User"]

admin.site.register(Order, AdminOrder)

admin.site.register(User_Detail)
