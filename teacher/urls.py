from django.urls import path
from . import views
app_name = 'teacher'
urlpatterns = [
        path('', views.index, name='index'),
        path('add/', views.teacher_add, name='teacher_add'),
        path('update/', views.teacher_update, name='teacher_update'),
    ]

