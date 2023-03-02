from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('populartiy/', views.my_view, name='my_view'),
    path('welcome/', views.my_view, name='welcome')
   
]
