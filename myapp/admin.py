from django.contrib import admin
from myapp.models import UserCreate, Product, Cart, Wishlist, Category, ProductRating, UserInfo

# Register your models here.

admin.site.register(UserCreate)


class Productadmin(admin.ModelAdmin):
    list_display = ['product_seller', 'product_collection', 'Product_category', 'product_size', 'product_color',
                    'product_price', 'product_description', 'product_image']
    search_fields = ['product_collection']


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Category)
admin.site.register(ProductRating)
admin.site.register(UserInfo)
