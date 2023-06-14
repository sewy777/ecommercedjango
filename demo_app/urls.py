from django.urls import path

from . import views

urlpatterns=[
    path("test/", views.firstapp),
    path("product/", views.show_products),
    path("addcategory/", views.post_category),
    path("addproduct/", views.post_product),
    path('showcategory/', views.show_category ),
    # FOR DELETING CATEGORY
    #showcategory
    # views ma delete_category function ma pathaucha
    path('deletecategory/<int:category_id>',views.delete_category),
    # FOR DELETING PRODUCT
    #index.html bata id pass bhayo => views ma gayo
    path("deleteproduct/<int:product_id>",views.delete_product),
    
    path('updatecategory/<int:category_id>',views.update_category),
    
    path('updateproduct/<int:product_id>',views.update_product),
    
    path('orderdetails/',views.order_details),
    
    path("userdetails/",views.show_users),
    
]

