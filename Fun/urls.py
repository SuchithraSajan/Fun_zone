from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_page, name='success'),
    path('first/',views.first,name='first'),
    path('tord/',views.tord,name='tord'),
    path('neon/',views.neon,name='neon'),
    path('chik/',views.chik,name='chik'),
]
