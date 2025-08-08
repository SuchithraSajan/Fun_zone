from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage or main view
    path('signup/', views.signup_view, name='signup'),
    path('welcome/',views.welcome,name='welcome'),
]
