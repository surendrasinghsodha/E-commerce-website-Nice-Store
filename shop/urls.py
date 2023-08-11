from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    # path('shop/', views.Shop.as_view(), name='shop'),
    path('product_view/', views.ShowProductView.as_view(), name='product_view'),
    path('product_detail/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),

    path('add_to_wishlist/<int:pk>/', views.AddProductToWishlist.as_view(), name='add_to_wishlist'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('remove_item/<int:pk>/', views.RemoveFromWishlist.as_view(), name='remove_item'),

    path('add_to_cart/<int:pk>/', views.AddProductToCart.as_view(), name="add_to_cart"),
    # path('cart/', views.CartView.as_view(), name='cart'),
    path('remove_from_cart/<int:pk>/', views.RemoveFromCart.as_view(), name='remove_from_cart'),

    path('cart_update/<int:pk>/', views.CartFormSetUpdateView.as_view(), name='cart_update'),

    path('user_info/', views.UserInfoView.as_view(), name='user_info'),
    path('order/', views.OrderView.as_view(), name='order')

]
