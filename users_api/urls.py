from django.urls import path
from users_api.views import Login, Signup, GetAccountDetails, UpdateAccount

urlpatterns = [
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
    path('get_account_details/<str:number>', GetAccountDetails.as_view()),
    path('update_account/<str:number>', UpdateAccount.as_view())
]
