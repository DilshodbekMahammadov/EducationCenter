"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mentors/', MentorListAPIView.as_view() ),
    path('mentors/<int:pk>/', MentorRetrieveUpdateDeleteAPIView.as_view() ),
    path('group/', GroupListAPIView.as_view() ),
    path('student/', StudentListAPIView.as_view() ),
    path('backend-group/', BackendGroupListAPIView.as_view() ),
    path('group/<int:pk>/', GroupRetrieveUpdateDeleteAPIView.as_view() ),
    path('student/<int:pk>/', StudentRetrieveUpdateDeleteAPIView.as_view() ),
]
