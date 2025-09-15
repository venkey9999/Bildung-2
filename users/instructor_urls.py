# users/instructor_urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_dashboard, name='instructor_dashboard'),
]
