from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('user/', views.user_list, name='index'),
    path('', views.login_user, name='login'),
    path('add/', views.user_add, name='user_add'),
    path('update/', views.user_update, name='user_update'),]