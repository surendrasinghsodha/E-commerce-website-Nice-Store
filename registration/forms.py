from django import forms
from django.contrib.auth.forms import UserCreationForm
# from myapp.models import UserCreate
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    CHOICES = (
        ('male', 'male'),
        ('female', 'female'),)
    gender = forms.ChoiceField(choices=CHOICES)
    usertype = forms.ChoiceField(choices=[
        ('user', 'user'),
        ('seller', 'seller')])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")


