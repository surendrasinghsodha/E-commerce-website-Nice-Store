from django import forms
from django.contrib.auth.models import User
from .models import Product, Category, ProductRating, Cart


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('product_seller',)

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)


class EditUSerProfile(forms.ModelForm):
    gender = forms.ChoiceField(choices=[
        ('male', 'male'),
        ('female', 'female')])

    usertype = forms.ChoiceField(choices=[
        ('user', 'user'),
        ('seller', 'seller')])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

        widgets = {
            'category_name': forms.TextInput(attrs={'Placeholder': 'Here create new category'})
        }


class ViewProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('product_seller',)


class ProductRatingForm(forms.ModelForm):
    class Meta:
        model = ProductRating
        fields = ('ratings', 'comments')
