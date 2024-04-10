from django.contrib import admin
from django.urls import path, include
from gamelands import views
appname = 'gamelands'
urlpatterns = [
    path('', views.return_index, name='index'),
]