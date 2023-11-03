from django.urls import path
from . import views as authp_views
from app import views as app_views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/',authp_views.register,name='register'),
    path('accounts/profile/',authp_views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),

    path('', app_views.home, name='home'),
    path('<int:id>/', app_views.post_detail, name='post_detail'),
    path('post/<int:id>/delete/', app_views.delete_post, name='delete_post'),
    path('post/create/', app_views.create_post, name='create_post'),

]