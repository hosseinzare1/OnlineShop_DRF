from django.urls import path
from shop.views import GetAllProducts, UpdateData, InsertProduct, Serach, Delete, GetImages

urlpatterns = [

    path('getall/', GetAllProducts.as_view()),

    path('get_images/', GetImages.as_view()),

    path('update/<int:key>', UpdateData.as_view()),
    path('insert/', InsertProduct.as_view()),
    path('search/', Serach.as_view()),
    path('delete/<int:pk>', Delete.as_view()),
]
