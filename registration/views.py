from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.urls import reverse

from myapp.models import UserCreate
from registration.forms import NewUserForm
from django.contrib import messages


# Create your views here
class Register(CreateView):
    form_class = NewUserForm
    template_name = 'registration/register.html'

    # success_url = 'login/'
    def get_success_url(self):
        return reverse('registration:login')

    def form_valid(self, form):
        self.object = form.save()
        UserCreate.objects.create(user=self.object, gender=form.cleaned_data['gender'],
                                  usertype=form.cleaned_data['usertype'])
        return super(Register, self).form_valid(form)


class Login(LoginView):
    template_name = 'registration/login.html'


class Logout(LogoutView):
    template_name = 'registration/logout.html'
