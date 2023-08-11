from django.urls import path
from registration import views
from django.views.generic.edit import CreateView

app_name = 'registration'
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
