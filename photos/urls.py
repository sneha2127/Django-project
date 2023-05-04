from django.urls import path
from .views import *

urlpatterns = [
    path('',gallery, name = 'gallery'),
    path('photo/<str:pk>/', view_photo, name='view-photo'),
    path('add/', addphoto, name='add-photo')

]