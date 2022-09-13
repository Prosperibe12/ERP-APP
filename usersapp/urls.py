from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views

"""
All urls for the users section of this application will be registered here
"""
# give a specific namespace to this urls to prevent namespace collision

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout', views.logout_view, name='logout'),
    
    # reset password settings
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='usersapp/reset_password.html'), name='reset_password'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='usersapp/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='usersapp/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='usersapp/password_reset_done.html'), name='password_reset_complete'),
]
