from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('follow/<str:username>/', views.follow_unfollow_view, name='follow_unfollow'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'), # Verify this name matches exactly
]