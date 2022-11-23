
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from stories.views import *
urlpatterns = [
    path('', index, name="index"),
    path('category/<int:pk>/', category, name="category"),
    path('story/<int:id>/', story, name="story"),
    path('contact/', contact, name="contact"),

]
