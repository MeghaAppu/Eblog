from django.urls import path
from .views import UserRegisterView #,UserLoginView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='registration'),
    #path('login/',UserLoginView.as_View(),name='login'),
   
]