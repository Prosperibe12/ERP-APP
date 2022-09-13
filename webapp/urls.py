from django.urls import path
from . import views

"""
All urls for the website section of this application will be registered here
"""
# give a specific namespace to this urls to prevent namespace collision
app_name = 'web'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_page, name='about'),
    path('services/', views.services_page, name='services'),
    path('contact/', views.contact_page, name='contact'),
    path('appointment/', views.appointment_page, name='appointment'),
    path('careers/', views.career_page, name='careers')
]