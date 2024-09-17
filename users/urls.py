'''define the URL models of users'''
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    # the page of login
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # logout
    path('logout/', views.logout_view, name='logout'),

    # register
    path('register/', views.register, name='register'),

]