from django.db import models

# Create your models here.

   
    
class Mattress_Product(models.Model):
    Image=models.ImageField(upload_to='image')
    Title=models.CharField(max_length=100)
    Product_Name= models.CharField(max_length=50)
    Product_Price=models.IntegerField()
    
    #
    Discount=models.IntegerField(default=0)
 
class Testmonial_Mattress(models.Model):
    Client_Name=models.CharField( max_length=50)
    Discription=models.CharField( max_length=500)
    Client_Image=models.ImageField(upload_to='images')    