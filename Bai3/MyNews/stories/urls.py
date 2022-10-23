from django.contrib import admin
from django.urls import path
from stories import views

urlpatterns = [
    path('', views.index, name='index'),
]
