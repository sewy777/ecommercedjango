from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages
# import to use login required and admin only
from django . contrib.auth.decorators import login_required
# from ..account.auth import admin_only
from account.auth import admin_only
# orderdetails
from users.models import *
#userdetail
from django.contrib.auth.models import User


# Create your views here.
def firstapp(request):
    return HttpResponse("This is my first app")

@login_required
@admin_only
def show_users(request):
    user=User.objects.all()
    context={
        "user":user
    }
    return render(request,"demo/userdetails.html",context)

@login_required
@admin_only
def show_products(request):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(request,"demo/index.html", context)

@login_required
@admin_only
def post_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, "Category added sucessfully")
            return redirect("/admin/addcategory")
        
        else:
            messages.add_message(request,messages.ERROR, "Category already exists, Please add a new category")
            return render(request,'demo/addcategory.html',{
                "form":CategoryForm
            })
    context={
    "form":CategoryForm
    }
    return render(request,'demo/addcategory.html', context)

@login_required
@admin_only
def post_product(request):
    # copied frm 
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, "Product added sucessfully")
            return redirect("/admin/addproduct")
        
        else:
            messages.add_message(request,messages.ERROR, "Product Not Added, Please try again")
            return render(request,'demo/addproduct.html',{
                "form":ProductForm
            })
    context={
        "form":ProductForm
    }
    return render(request,'demo/addproduct.html',context)

@login_required
@admin_only
def show_category(request):
    category=Category.objects.all()
    context={
        "category":category
    }
    return render(request, "demo/showcategory.html",context)

# FOR DELETING CATEGORY
#
@login_required
@admin_only
def delete_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,"Category Deleted")
    #redirect le kei kaam bhaye pachi tyo link ma pathaucha
    return redirect("/admin/showcategory")

#FOR DELETEING PRODUCT
#id ko product liyo => ani delete garyo
@login_required
@admin_only
def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,"Product Deleted")
    return redirect("/admin/product")



# FOR EDIT
@login_required
@admin_only
def update_category(request,category_id):
    category=Category.objects.get(id=category_id)
    
    # copied from up/addcategory
    
    if request.method=="POST":
        # instance=category le change garcha
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, "Category Edited Sucessfully")
            return redirect("/admin/showcategory")
        
        else:
            messages.add_message(request,messages.ERROR, "Category already exists, Please add a new category")
           #made changes
            # return render(request,'demo/updatecategory.html',{
            return render(request,'demo/updatecategory.html',{
                # Categoryform lai from banayo
                "form":form
            })
    context={
    "form":CategoryForm(instance=category)
    }
    # 
    # return render(request,'demo/updatecategory.html', context)
    return render(request,'demo/updatecategory.html', context)

# copied from up/post_product
@login_required
@admin_only
def update_product(request,product_id):
    # euta matra update garna id get
    #id stored in product 
    product=Product.objects.get(id=product_id)
    
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, "Product Updated Sucessfully")
            # product bhane showproduct cha urls ma
            return redirect("/admin/product")
        
        else:
            messages.add_message(request,messages.ERROR, "Product Update Unsuccessful, Please try again")
            return render(request,'demo/updateproduct.html',{
                # productform ko satt form
                "form":form
            })
    context={
        # instance shows the stored date in product
        "form":ProductForm(instance=product)
    }
    return render(request,'demo/updateproduct.html',context)

# after copy pasting index.html to orderdetails
@login_required
@admin_only
def order_details(request):
    detail=Order.objects.all()
    context={
        "detail":detail
        
    }
    return render (request,'demo/orderdetails.html',context)