from django.db import models
from django.contrib.auth.models import User
from time import timezone


# Create your models here.

class UserCreate(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # additional fields
    gender = models.CharField(max_length=20,
                              choices=[('male', 'Male'),
                                       ('female', 'Female')])
    usertype = models.CharField(max_length=100, choices=[
        ('user', 'User'),
        ('seller', 'Seller')])

    def __str__(self):
        return self.user.username + "-" + self.usertype


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


# make model for collection
# make model for size
# make model for color


class Product(models.Model):
    CHOICE1 = (
        ('men', 'Men'),  # {{ i.get_product_collection_display }} in this way capital Men ll show
        ('women', 'Women'),)

    CHOICE3 = (
        ('m', 'M'),
        ('l', 'L'),
    )
    CHOICE4 = (
        ('red', 'Red'),
        ('black', 'Black'),
        ('blue', 'Blue'),
    )

    product_seller = models.ForeignKey(UserCreate, on_delete=models.CASCADE)
    product_collection = models.CharField(max_length=100, choices=CHOICE1)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=100, choices=CHOICE3)
    product_color = models.CharField(max_length=100, choices=CHOICE4)
    product_price = models.PositiveIntegerField()
    product_description = models.TextField()
    product_image = models.ImageField(upload_to="product_image/")

    def __str__(self):
        return self.product_seller.user.first_name + "_" + self.product_collection + "_" + self.product_category.category_name


class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserCreate, on_delete=models.CASCADE)
    ratings = models.IntegerField(
        choices=[(1, 'Good'), (2, 'Very Good'), (3, 'Great'), (4, 'Excellent'), (5, 'Outstanding')])
    comments = models.TextField()

    def __str__(self):
        return self.user.user.first_name + "_" + self.product.product_collection


class Wishlist(models.Model):
    user = models.ForeignKey(UserCreate, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.first_name + "_" + self.product.product_collection


class Cart(models.Model):
    user = models.ForeignKey(UserCreate, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    product_qty = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()

    def __str__(self):
        return self.user.user.first_name + "_" + self.product.product_collection


class UserInfo(models.Model):
    user = models.ForeignKey(UserCreate, on_delete=models.CASCADE)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
