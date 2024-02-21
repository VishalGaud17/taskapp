from django.urls import path
from authapp import views

urlpatterns = [
    # path('authapp/login',views.user_login),
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
]