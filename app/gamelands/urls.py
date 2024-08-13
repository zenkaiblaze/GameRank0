from django.contrib import admin
from django.urls import path, include
from gamelands import views
app_name = 'gamelands'
urlpatterns = [
    path('', views.return_index, name= 'index'),
    path('cabinet/', views.return_cabinet, name = 'cabinet'),
    path('mgs/', views.return_mgs, name='mgs' ),
    path('base-game/', views.return_base_game_page, name = 'base-game'),
    path('base/', views.get_base_page, name = 'base'),
    path("<int:game_id>", views.get_title_page, name = 'titlepage'),
    path('login/', views.login_page, name = "login"),
    path('registration/', views.registration_page, name = "registration"),
    path('counter/', views.page, name= 'counter'),
    path('excel/', views.excel_page, name = 'excel'),
    path('search/', views.search_page, name = 'search'),

]