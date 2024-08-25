from django.contrib import admin
from django.urls import path, include
from gamelands import views

from gamelands.all_views import search_page_view, profile_upload_form_view
app_name = 'gamelands'
urlpatterns = [
    path('', views.return_index, name= 'index'),
    #path('cabinet/', views.return_cabinet, name = 'cabinet'),
    path('cabinet/', profile_upload_form_view.profile_upload_form, name = 'cabinet'),
    path('mgs/', views.return_mgs, name='mgs' ),
    path('base-game/', views.return_base_game_page, name = 'base-game'),
    path('base/', views.get_base_page, name = 'base'),
    path("<int:game_id>", views.get_title_page, name = 'titlepage'),
    path('login/', views.login_page, name = "login"),
    path('registration/', views.registration_page, name = "registration"),
    path('counter/', views.page, name= 'counter'),
    path('excel/', views.excel_page, name = 'excel'),
    #path('search/', views.search_page, name = 'search'),
    path('search/', search_page_view.search_page, name = 'search'),

]