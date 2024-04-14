from django.contrib import admin
from django.urls import path, include
from .views import home,borgona,batman

urlpatterns = [
    path('', home, name="home"),
    path('borgona',borgona,name="borgona"),
    path('batman', batman, name="batman"),
]