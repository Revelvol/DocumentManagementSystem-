"""QMS URL Configuration
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.userRegister, name="userRegister"),
    path('login/', views.userLogin, name="userLogin"),
    path('logout/', views.userLogout, name="userLogout"),
    path('editUserMenu/', views.editUserMenu, name="editUserMenu"),
    path('editUser/<str:pk>', views.editUser, name="editUser"),
    path('viewUser/<str:pk> ', views.viewUser, name="viewUser"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/ ', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_validation/', views.password_validation, name='passwordValidation'),
    path('delete_user/<pk>', views.deleteUser, name='deleteUser'),
    path('edit_position/', views.editPosition, name='editPosition'),
]
