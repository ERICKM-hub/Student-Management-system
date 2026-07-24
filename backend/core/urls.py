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
