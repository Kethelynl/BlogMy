from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.registrar, name='registrar'),
    path('logout/', views.logout_views, name='logout')
]