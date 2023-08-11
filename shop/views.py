from django.shortcuts import redirect
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from shop.forms import CartForm, UserInfoForm
from myapp.models import Product, Wishlist, Cart, UserInfo
from django.contrib import messages
from django.forms import modelformset_factory
from django.urls import reverse


class ShowProductView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'  # in html data display from this name


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'userdata'

    def get_context_data(self, **kwargs):  # if add then  remove button appear---> if in product_detail.html
        context = super().get_context_data(**kwargs)
        context['wishlist_obj'] = Wishlist.objects.filter(user=self.request.user.usercreate,
                                                          product=self.object).first()

        context['cart_obj'] = Cart.objects.filter(user=self.request.user.usercreate,
                                                  product=self.object).first()
        return context


class AddProductToWishlist(LoginRequiredMixin, View):

    def post(self, request, **kwargs):
        user = self.request.user.usercreate  # LOGIN USER
        product = Product.objects.get(id=self.kwargs.get('pk'))  # to fetch the id's data from Product model
        Wishlist.objects.create(user=user, product=product)  # to save the data
        messages.success(request, " Product has been added to the wishlist !! ")  # print through for loop in html
        return redirect('shop:product_detail', product.id)  # kwargs we use only in reverse!! to stay that same page
        # return redirect('shop:product_view')  # to go again in shop page


class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist/wishlist.html'

    def get_context_data(self, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        context["wishlist_count"] = len(self.model.objects.filter(user=self.request.user.usercreate))
        # take len of data in the name of wishlist_count print at the sidebar

        # context['cart_object'] = Cart.objects.filter(user=self.request.user.usercreate,
        #                                              product=self.object_list)
        return context


class RemoveFromWishlist(LoginRequiredMixin, View):

    def post(self, request, **kwargs):
        user = self.request.user.usercreate  # login user
        wishlist_item = Wishlist.objects.get(user=user, id=self.kwargs.get('pk'))
        wishlist_item.delete()
        messages.success(request, 'Product has been removed successfully')
        return redirect('shop:wishlist')


# when we click on cart-button from product_detail.html at that time it save product in the backend
# and now we ll make list view to show that data that is CartView
class AddProductToCart(LoginRequiredMixin, View):

    def post(self, request, **kwargs):
        user = self.request.user.usercreate
        product = Product.objects.get(id=self.kwargs.get('pk'))
        product_qty = 1
        total_price = product.product_price * product_qty
        Cart.objects.create(user=user, product=product, product_qty=product_qty, total_price=total_price)
        messages.success(request, " Product has been added to the Cart !! ")
        return redirect('shop:product_detail', product.id)


class RemoveFromCart(LoginRequiredMixin, View):
    def post(self, request, **kwargs):
        user = self.request.user.usercreate
        cart_item = Cart.objects.get(user=user, id=self.kwargs.get('pk'))
        cart_item.delete()
        messages.success(request, 'Product has been removed successfully')
        return redirect('shop:product_view')


#  ---------------------------->   FORMSET  CART  <--------------------------
# class CartFormSetView(View):
#     template_name = 'cart/cart.html'
#
#     def get(self, request):
#         CartFormSet = modelformset_factory(Cart, form=CartForm, extra=0)
#         formset = CartFormSet(queryset=Cart.objects.filter(user=request.user.usercreate))
#         return render(request, self.template_name, {'formset': formset})
#
# def post(self, request):
#     CartFormSet = modelformset_factory(Cart, form=CartForm, extra=1)
#     formset = CartFormSet(request.POST)
#     if formset.is_valid():
#         formset.save()
#         return redirect('shop:product_view')
#     return render(request, self.template_name, {'formset': formset})
# -----------------------above code converted ----------------------


class CartFormSetUpdateView(LoginRequiredMixin, UpdateView):
    model = Cart
    template_name = 'cart/cart.html'
    fields = []

    def get_success_url(self):
        return reverse('shop:user_info')
        # return reverse('shop:cart_update', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        CartFormSet = modelformset_factory(Cart, form=CartForm, extra=0)
        if self.request.POST:
            cart_formset = CartFormSet(self.request.POST,
                                       queryset=Cart.objects.filter(user=self.request.user.usercreate),
                                       prefix='cart_formset')  # when Id generate at that time start with prefix name

        else:
            cart_formset = CartFormSet(queryset=Cart.objects.filter(
                user=self.request.user.usercreate),
                prefix='cart_formset')  # queryset =user's data take from backend & show in table
        context['total_items'] = len(self.model.objects.filter(user=self.request.user.usercreate))  # count total item
        context['cart_formset'] = cart_formset

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['cart_formset']
        if formset.is_valid():
            for form in formset:
                form.instance.user = self.request.user.usercreate
                form.save()
        return super().form_valid(form)


class UserInfoView(LoginRequiredMixin, CreateView):
    model = UserInfo
    form_class = UserInfoForm
    template_name = 'cart/userinfo.html'

    def get_success_url(self):
        return reverse('shop:order')

    def form_invalid(self, form):
        print(">>>>>>>>", form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print(">>>>>>>>", form.errors)
        if form.is_valid():
            form.instance.user = self.request.user.usercreate
        return super().form_valid(form)


class OrderView(TemplateView):
    template_name = 'cart/order.html'

# messages.success("Your information has been submitted")
