from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.main, name = 'index'),
    path('view-orders/', views.view_orders, name = 'view_orders'),
    path('admin_page/', views.admin_page, name='admin_page')
]