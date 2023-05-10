from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('upload/top/', views.upload_top, name='upload_top'),
    path('upload/bottom/', views.upload_bottom, name='upload_bottom'),
]
