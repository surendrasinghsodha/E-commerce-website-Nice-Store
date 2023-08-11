from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (ListView, CreateView, DetailView, DeleteView)
from django.views.generic import UpdateView
from django_filters.views import FilterView

from myapp.models import Product, Category, ProductRating
from .filters import ProductFilter
from .forms import ProductAddForm, EditUSerProfile, CategoryForm, ViewProductUpdateForm, ProductRatingForm
from django.contrib.auth.models import User
from django.urls import reverse
from django_tables2 import SingleTableView
from myapp.tables import CategoryTable, ViewProductTable


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/home.html'


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductAddForm
    template_name = 'myapp/seller/seller_add_product.html'

    # success_url = 'index'
    def get_success_url(self):
        return reverse('view_product')

    def form_valid(self, form):
        print(form.errors)
        if form.is_valid():
            form.instance.product_seller = self.request.user.usercreate  # to (save)get login user
        return super().form_valid(form)


# class ProductView(ListView): #this code i change into ViewProductTableList
#     model = Product
#     template_name = 'myapp/seller/view_product.html'
#
#     def get_queryset(self):  # to show data who iis login
#         query = super().get_queryset()
#         query = query.filter(product_seller=self.request.user.usercreate)
#         return query


class SellerDetailView(DetailView):
    model = Product
    template_name = 'myapp/seller_detail.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditUSerProfile
    template_name = 'myapp/profile_detail.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs.get('pk')})  # this kwargs to say in same page with pk


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'myapp/category/add_category.html'

    def get_success_url(self):
        return reverse('category')

    def form_valid(self, form):
        if form.is_valid():
            form.instance.created_by = self.request.user  # in created_by ->save the login user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'myapp/category/update_category.html'

    def get_success_url(self):
        return reverse('category')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'myapp/category/delete_category.html'

    def get_success_url(self):
        return reverse('category')


class CategoryTableList(LoginRequiredMixin, SingleTableView):
    model = Category
    table_class = CategoryTable
    template_name = 'myapp/category/category.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(created_by=self.request.user)  # show only login user data
        return query


class ViewProductTableList(LoginRequiredMixin, FilterView, SingleTableView):
    model = Product
    table_class = ViewProductTable
    template_name = 'myapp/seller/view_product.html'
    filterset_class = ProductFilter

    def get_queryset(self):  # to show only login user data
        query = super().get_queryset()
        query = query.filter(
            product_seller=self.request.user.usercreate)  # use createuser+ model bcz  it has  that model foreign key
        return query

    def get_context_data(self, **kwargs):  # this is for if condition for clear in =  {% if has_filter %}
        context = super(ViewProductTableList, self).get_context_data(**kwargs)
        f = context['filter']
        has_filter = any(field in self.request.GET for field in set(f.get_fields()))
        context['has_filter'] = has_filter
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ViewProductUpdateForm
    template_name = 'myapp/seller/update_product.html'

    def get_success_url(self):
        return reverse('view_product')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'myapp/seller/delete_product.html'

    def get_success_url(self):
        return reverse('view_product')


class ProductRatingView(LoginRequiredMixin, CreateView):
    model = ProductRating
    form_class = ProductRatingForm
    template_name = 'myapp/rating/product_rating.html'

    def get_success_url(self):
        return reverse('view_product')

    def form_valid(self, form, ):
        print(form.errors)
        if form.is_valid():
            form.instance.user = self.request.user.usercreate
        return super().form_valid(form)

# class ProfileDetailView(DetailView):
#     Model = UserCreate
#     template_name = 'myapp/profile_detail.html'
#     queryset = UserCreate.objects.all()
#
#     # context_object_name = 'userdata'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = UserCreate.objects.get(id=self.kwargs.get('pk'))
#         return context
