from django.urls import path
from shop.views import GetAllProducts, UpdateData, InsertProduct, Delete, GetImages, GetProduct, GetGroups, \
    GetCategorys, GetProductAttributes, GetProductsByCategory, Search, GetComments, SubmitComment, GetSameProducts, \
    GetSpecialDiscount

urlpatterns = [

    path('getall/', GetAllProducts.as_view()),
    path('get_products_by_category/<int:category_id>', GetProductsByCategory.as_view()),
    path('get_same_products/<int:product_id>', GetSameProducts.as_view()),
    path('get_product/<int:key>', GetProduct.as_view()),
    path('get_images/<int:key>', GetImages.as_view()),
    path('get_comments/<int:key>', GetComments.as_view()),
    path('submit_comment/', SubmitComment.as_view()),
    path('get_special_discounts/', GetSpecialDiscount.as_view()),

    path('get_groups/', GetGroups.as_view()),
    path('get_categorys/<int:group_key>', GetCategorys.as_view()),

    path('get_product_attributes/<int:product_key>', GetProductAttributes.as_view()),

    path('update/<int:key>', UpdateData.as_view()),
    path('insert/', InsertProduct.as_view()),
    path('search_product/<str:search_text>', Search.as_view()),
    path('delete/<int:pk>', Delete.as_view()),
]
