from django.urls import path
from . import views

#add all the paths that you want ( path, render from views.py, name of URL)

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]