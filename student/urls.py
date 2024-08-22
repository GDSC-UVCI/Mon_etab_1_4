from  django.urls import path
from . import views

app_name='student'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.student_add, name='student_add'),
    path('update/', views.student_update, name='student_update'),
]

