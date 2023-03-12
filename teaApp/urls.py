from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name = 'index'),
    path('view-orders/', views.view_orders, name = 'view_orders')
]