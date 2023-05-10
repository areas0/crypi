from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='default'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('vote/', views.vote, name="vote"),
    path('result/', views.result, name="result")
]
