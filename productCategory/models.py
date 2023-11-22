from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product_Category(models.Model):
    name= models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name
    
class Header_ProductButton(models.Model):
    product_name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.product_name

# making the model for mattress size
class Size(models.Model):
    TypeOfSize=models.CharField(max_length=30)
    
    def __str__(self):
        return self.TypeOfSize    
        
class Product_Card(models.Model):
    Image= models.ImageField(upload_to='images')  
    Productname= models.CharField( max_length=50) 
    Title=models.CharField(max_length=100, default=True)
    Productprice= models.IntegerField()
    Discount=models.IntegerField(default=0)
   
    productCategory = models.ForeignKey(Product_Category, on_delete=models.DO_NOTHING, null=True) 


    def __str__(self) -> str:
        return self.Productname

class Testmonial(models.Model):
    Client_Name=models.CharField( max_length=50)
    Discription=models.CharField( max_length=500)
    Client_Image=models.ImageField(upload_to='images')
    product_category= models.ForeignKey(Product_Category, on_delete=models.DO_NOTHING, null=True)
    
class Facility(models.Model):
    Image= models.ImageField(upload_to='images')
    Facility_Name= models.CharField(max_length=100)
    Discription= models.CharField(max_length=500)
    
class Client_Rating(models.Model):
    Date= models.DateField(auto_now_add=True)
    Client_Name= models.CharField(max_length=50)
    Discription=models.CharField(max_length=500)
    product_category= models.ForeignKey(Product_Category, on_delete=models.DO_NOTHING, null=True) 
    # OnlineCompanyImage= models.ImageField(upload_to='images')

class Size(models.Model):
    size=models.CharField(max_length=20, default=0)    
    product_category= models.ForeignKey(Product_Category, on_delete=models.DO_NOTHING, null=True)
    
#making the model for cart
class Cart(models.Model):
    product= models.ForeignKey(Product_Card, on_delete=models.DO_NOTHING, null=True)
    productCategory= models.ForeignKey(Product_Category, on_delete=models.DO_NOTHING, null=True)
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    Date= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.product.Productname + str("hello")

# making the fuction for buy product 
class Order(models.Model):
    Product= models.ForeignKey(Product_Card, on_delete=models.DO_NOTHING, null=True )
    Product_category= models.ForeignKey(Product_Category, on_delete=models.DO_NOTHING, null=True)
    User= models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    Order_Date= models.DateTimeField(auto_now_add=True)
    Shipping_Date= models.DateTimeField(auto_now_add=True)
    Payment_Mode= models.CharField(max_length=50)
    
# making the model for user detail
class User_Detail(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user= models.OneToOneField(User, null=True, blank=True, on_delete=models.DO_NOTHING,)
    phone_number= models.IntegerField()
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    pincode= models.IntegerField()
    
    def __str__(self) -> str:
        return self.user.username 