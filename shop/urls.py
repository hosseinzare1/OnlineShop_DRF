from django.urls import path
from shop.views import GetAllData, GetFavData, UpdateData, InsertProduct, Serach, Delete,getAll

urlpatterns = [

    path('getall/', GetAllData.as_view()),
    path('getalldef/', getAll),
    path('getfav/', GetFavData.as_view()),
    path('update/<int:key>', UpdateData.as_view()),
    path('insert/', InsertProduct.as_view()),
    path('search/', Serach.as_view()),
    path('delete/<int:pk>', Delete.as_view()),
]
