"""
URL configuration for employment_empower project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('users', users, name='users'),
    path('memberships', memberships, name='membership_list'),
    path('job-seekers', job_seekers, name='job_seekers'),
    path('job-seekers/details', job_seeker_detail, name='seeker_details'),
    path('content', content, name='content'),
    path('private-sessions', meetings, name='meetings'),
    path('feedback-and-queries', feedback, name='feedback'),
    path('orders', orders, name='orders'),
    path('coupons', coupons, name='coupons'),
]
