from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage or main view
    path('next/', views.next_page, name='next'),  # for your next page
]
