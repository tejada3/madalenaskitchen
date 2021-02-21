from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [

    path('', views.menu, name='menu'),
    path('login/', views.Login, name='login'),
    path('menu-controls/', views.menucontrol, name='menu-controls'),
    path('changeav/<str:pk>', views.menuchangeavailablity, name='changeav'),
    path('av/<str:pk>', views.changeavailability, name='av'),
    path('update/<str:pk>', views.editMenu, name='update'),
    path('add/', views.addToMenu, name='add'),
    path('addd/', views.addFOTW, name='addd'),
    path('delete/<str:pk>', views.deleteitem, name='delete'),
    path('deleteFOTW/<str:pk>', views.deleteFOTW, name='deleteFOTW'),

]