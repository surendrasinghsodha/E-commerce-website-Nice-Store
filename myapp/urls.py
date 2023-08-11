from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('seller_add_product/', views.AddProduct.as_view(), name='seller_add_product'),
    # path('product_view/', views.ProductView.as_view(), name='product_view'),

    path('view_product_user/', views.ViewProductTableList.as_view(), name='view_product'),
    path('product_update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', views.ProductDeleteView.as_view(), name='p_delete'),
    path('post_detail/<int:pk>/', views.SellerDetailView.as_view(), name='post_detail'),
    # path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile_edit/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile'),

    path('category/', views.CategoryTableList.as_view(), name='category'),
    path('category_create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('rating/', views.ProductRatingView.as_view(), name='product_rating'),

]
