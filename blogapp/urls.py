from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.blog_create, name='blog_create'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('edit/<int:pk>/', views.blog_update, name='blog_update'),
    path('delete/<int:pk>/', views.blog_delete, name='blog_delete'),
]
