from django import forms
from myapp.models import Wishlist
from myapp.models import Cart, UserInfo, User


# ---------------------------->   FORMSET  CART  <--------------------------
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product_qty', 'total_price']

    def __init__(self, *args, **kwargs):  # user not able to edit
        super().__init__(*args, **kwargs)
        self.fields['total_price'].widget.attrs['readonly'] = True


class UserInfoForm(forms.ModelForm):
    # address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))  for addition_field widgets--OR-->

    class Meta:
        model = UserInfo
        fields = ('address', 'pincode', 'city', 'state')

        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 4}),
        }
