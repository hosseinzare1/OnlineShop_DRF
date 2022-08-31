from django.urls import path
from shop.views import GetAllProducts, UpdateData, InsertProduct, Delete, GetImages, GetProduct, GetGroups, \
    GetCategorys, GetProductAttributes, GetProductsByCategory, Search, GetComments, SubmitComment, GetSameProducts, \
    GetSpecialDiscounts, GetBestselling, SubmitOrder, GetProductsByGroup, GetOrders, GetUserComments, GetOrderDetails, \
    EditComment, DeleteComment,GetNewsImages

urlpatterns = [

    path('get_news_images/', GetNewsImages.as_view()),
    path('get_all/', GetAllProducts.as_view()),
    path('get_special_discounts/', GetSpecialDiscounts.as_view()),
    path('get_bestselling/', GetBestselling.as_view()),

    path('get_groups/', GetGroups.as_view()),
    path('get_categories/<int:group_key>', GetCategorys.as_view()),
    path('get_products_by_category/<str:category>', GetProductsByCategory.as_view()),
    path('get_products_by_group/<str:group>', GetProductsByGroup.as_view()),
    path('get_same_products/<int:product_id>', GetSameProducts.as_view()),

    path('get_product/<int:key>', GetProduct.as_view()),
    path('get_images/<int:key>', GetImages.as_view()),
    path('get_comments/<int:key>', GetComments.as_view()),
    path('get_product_attributes/<int:product_key>', GetProductAttributes.as_view()),

    path('delete_comment/<int:key>', DeleteComment.as_view()),
    path('edit_comment/<int:key>', EditComment.as_view()),
    path('get_user_comments/<int:user_number>', GetUserComments.as_view()),
    path('submit_comment/', SubmitComment.as_view()),
    
    path('submit_order/', SubmitOrder.as_view()),
    path('get_orders/<int:user_number>', GetOrders.as_view()),
    path('get_order_details/<int:order_id>', GetOrderDetails.as_view()),


    path('update/<int:key>', UpdateData.as_view()),
    path('insert/', InsertProduct.as_view()),
    path('search_product/<str:search_text>', Search.as_view()),
    path('delete/<int:pk>', Delete.as_view()),
]
