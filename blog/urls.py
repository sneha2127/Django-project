from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('addpost/', user_add_post, name='addpost'),
    path('updatepost/<int:id>/', user_update_post, name='updatepost'),
    path('deletepost/<int:id>/', user_delete_post, name='deletepost'),
    path('userlogin/', user_login, name='userlogin'),
    path('signup/', user_signup, name='signup'),
    path('userlogout/', user_logout, name='userlogout'),

    
]