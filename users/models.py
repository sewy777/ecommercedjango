from django.db import models

from demo_app.models import *

from tkinter import CASCADE

from django.contrib.auth.models import User


# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

# total price
# tuple
# tuple ma duplicate item hudaina
class Order(models.Model):
    PAYMENT=(
        ("Cash on Delivery","Cash on Delivery"),
        ("Esewa","Esewa"),
        ("Khalti","Khalti"),
        
        
        
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    status=models.CharField(default='Pending',max_length=200,null=True)
    payment_method=models.CharField(max_length=200,choices=PAYMENT,null=True)
    payment_status=models.BooleanField(default=False,null=True)
    contact_no=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    order_date=models.DateTimeField(auto_now_add=True)


