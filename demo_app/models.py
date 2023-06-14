from django.db import models

# Create your models here.

class Category(models.Model):
    # unique=True => primary key
    #unique=true na garre bhaye id / ra category feri milcha same name halna dincha
    category_name=models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    product_stock=models.IntegerField()
    # img_url=models.CharField(max_length=200)
    product_image=models.FileField(upload_to='static/uploads',null=True)
    product_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    # Category lai foreign key banako
    #foreign key => connect two tables
    #category delete => models.cascade => saab delete
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.product_name
    
