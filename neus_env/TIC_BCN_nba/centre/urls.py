from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.index_profes, name='index_profes'),
    path('students', views.index_alumnat, name='index_alumnat'),
    path('user-form/', views.user_form, name='user-form')
]