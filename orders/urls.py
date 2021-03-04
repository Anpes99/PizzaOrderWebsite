from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register', views.register, name="register"),
    path('register1', views.register1, name="register1"),
    path('loginuser', views.login, name="loginuser"),
    path('confirmCart',views.confirmCart, name="confirmCart"),
    path('orderConfirmed', views.orderConfirmed, name="orderConfirmed"),
    path('addItem', views.addItem, name="addItem")
]
