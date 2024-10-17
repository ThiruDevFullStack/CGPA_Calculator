"""
URL configuration for Myproject project.

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

from Myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="home"),
    path('gradeTable/',views.gradeTable,name="gradeTable"),
    path('cgpa_cal/',views.cgpa_calculation,name="cgpa_cal"),
    path('cgpa_cal_six/',views.cgpa_calculation_sixSem,name="cgpa_cal_six"),
    path('cgpa_percentage/',views.cgpa_percentage,name="cgpa_percentage"),
]
