from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage or main view
    path('sign/', views.sign, name='sign'), 
    path('welcome/',views.welcome,name='welcome'),
]
