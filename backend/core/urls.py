"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from rest_framework_simplejwt.views import TokenVerifyView
from django.contrib import admin
from django.urls import path,include
from main.models import *
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/users/',views.Users_view,name="users"),
    path('api/instructors/',views.Instructors,name="instructors"),
    path('api/department/',views.department,name="department"),
    path('api/students/',views.Students,name="students"),
    path('api/academicYear/',views.AcademicYear,name="year"),
    path('api/semester/',views.Semester,name="semester"),
    path('api/courses/',views.course,name='courses'),
    path('api/courseSection/',views.courseSection,name="courseSection"),
    path('api/enrollment/',views.enrollment,name="enrollment"),
    path('api/grades/',views.grade,name='grades'),
    path('api/attendance/',views.attendance,name="attendance"),
    path('api/feePayment/',views.feePayment,name="feePayment"),
]
