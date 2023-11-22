from django.shortcuts import render,redirect
from django.http import HttpResponse
from productCategory.models import Product_Category, Product_Card, Testmonial,\
    Facility, Client_Rating, Header_ProductButton,Size, \
    Cart,Order, User_Detail

from django.contrib import auth

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == "GET":
        section = request.GET.get('section')
       # pillow = request. GET.get("pillow")
        print("Current Section: ")
        cards  = None
        if section:
            cards = Product_Card.objects.filter(productCategory__name = section)
        else:
            cards= Product_Card.objects.all()
   
    productCategories= Product_Category.objects.all()
    
    testimonial=Testmonial.objects.all()
    facility= Facility.objects.all()
    clientRating= Client_Rating.objects.all()
    header_button=Header_ProductButton.objects.all()
    
    return render(request, 'home.html',{"productCategories": productCategories, "cards": cards, "testimonial": testimonial, "facility": facility, "clientRating": clientRating, 'header_button':header_button})

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request,user)
            else :
                return render(request, 'access denied.html')
    return redirect("home")
def logout(request):
    print("loging out")
    auth.logout(request)
    return redirect("login")  
def contact(request):
    return render(request, 'contact.html')

# making the view for shop now or product details

def productDetail(request, pk):
    
    request.GET.get("pc")
    size= Size.objects.filter(product_category__name="Pillow")
    if request.method=="GET":
        productCard= Product_Card.objects.get(id=pk)    
        
        if request.GET.get("op") == "addToCart":
            return add_to_cart(request)
           
        return render(request, 'shopNow.html', {"pro_card":productCard, 'size':size})


# making the function for register
def register(request):
    if request.method=="GET":
        return render(request, "register.html")
    if request.method=="POST":
        print("request data:", request.POST)
        user= User_Detail()
        user.phone_number= request.POST['phone_number']
        
        user.address= request.POST['address']
        user.pincode=request.POST['pincode']
        user.user = request.user
        user.save()
        
        
    return render(request, "register.html")

# making the function for cart
def cart(request):
    cartitems= Cart.objects.all()
    
    return render(request, "cart.html",{"CartItems":cartitems})

        
def addCart(request):
    if request.method == "GET":
        print(request.path)
        return render(request, "shopNow.html")
   
        
    
def add_to_cart(request):
    
    product_category = request.GET.get("productCategory")
    product_id = request.GET.get("id")
    
    cart_item = Cart()
    
    cart_item.product = Product_Card.objects.get(pk=int(product_id))
    cart_item.productCategory = Product_Category.objects.get(name=product_category.capitalize())
    cart_item.user = request.user
    
    cart_item.save()
    
    return redirect("productDetail", pk=int(product_id) ) 
    
     
     
#  function for enter button 
def searchQuery(request):
    
    if request.method=="GET":
        query = request.GET.get("query")
        result = Product_Card.objects.filter(Productname__icontains=query)
        print()
        if len(result) == 0:
            return HttpResponse("No result found")
        else:
            print(result)
            
        
    
    return render(request,"searchQuery.html" ,{"cards": result}) 

# function for buy now page

    
    
# making the fuction for buy  now 
def order_detail(request):
    
    product_category = request.GET.get("Product_category")
    product_id = request.GET.get("id")
    
    order= Order()
    
    order.Product = Product_Card.objects.get(pk=int(product_id))
    order.Product_category = Product_Category.objects.get(name=product_category.capitalize())
    order.User = request.user
    
    order.save()

    
    return redirect("productDetail", pk=int(product_id) )     
        
        
        

#making the function for to delete the card
def delete(request, pk):
    if request.method=="GET":
        print("button pressed", pk)
        cart= Cart.objects.get(pk=pk)
        cart.delete()
    return redirect("cart")

# making the function for user detail
# def user_detail(request):

# making the function for profile
def profile(request,pk ):
    user=User_Detail.objects.get(user=pk)
    print("user id",User_Detail.id)
    return render(request, "profile.html", {"User":user})

# now we making the fuction for editing the profile
def edit(request,pk):
    if request.method=="GET":
        user=User_Detail.objects.get(user=pk)
        return render(request, "editProfile.html" ,{"user":user})
    if request.method=="POST":
        print("request data:", request.POST)
        user=User_Detail.objects.get(user=pk)
        user.user=request.POST["user"]
        user.phone_number= request.POST['phone_number']
        user.email=request.POST["email"]
        user.address= request.POST['address']
        user.pincode=request.POST['pincode']
        user.user = request.user
        user.save()
        
        return redirect("profile")
        
def buyNow(request, pk ):
    buy = Product_Card.objects.get(id=pk)
    year=[2023,2024]
    
    return render(request, "buyNow.html", {"Buy": buy , "year":year})


    
    
    
    
    

    