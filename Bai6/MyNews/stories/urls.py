
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path
from stories.views import *
urlpatterns = [
    path('index/', index, name="index"),
    path('blog/', blog, name="blog"),
    path('Contact_us/', Contact_us, name="Contact_us"),
    path('single/', single, name="single"),
]
