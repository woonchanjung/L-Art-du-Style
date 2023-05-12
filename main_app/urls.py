from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clothes/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('clothes/upload_top/', views.upload_top, name='upload_top'),
    path('clothes/upload_bottom/', views.upload_bottom, name='upload_bottom'),
    path('clothes/create_match/', views.create_match, name='create_match'),
    path('clothes/view_matches/', views.view_matches, name='view_matches'),
    path('clothes/<int:top_id>/delete/', views.delete_top, name='delete_top'),
    path('clothes/<int:bottom_id>/delete/', views.delete_bottom, name='delete_bottom'),
]
