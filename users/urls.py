from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='editprofile'),
    path('profile/delete/',views.delete_profile,name='deleteprofile'),
    path('profile/changepswd/',views.change_password,name='changepswd'),
    
   
]