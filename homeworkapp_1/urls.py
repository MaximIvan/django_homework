from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('about_me/', views.about_me, name='about_me'),
]