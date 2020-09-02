from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),

]