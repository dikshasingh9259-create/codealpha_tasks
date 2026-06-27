from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_post_view, name='create_post'),
    path('user/<str:username>/', views.profile_view, name='profile'),
    path('like/<int:post_id>/', views.like_post_view, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment_view, name='add_comment'), 
    path('search/', views.search_users_view, name='search_users'),
]