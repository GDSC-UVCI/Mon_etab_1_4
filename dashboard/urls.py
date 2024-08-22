from django.urls import path
from . import views
from user.views import login_user
from .views import index

app_name = 'dashboard'
urlpatterns = [
    path('', index, name='index'),
    path('rapport/', views.report, name='report'),
]