from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "role",
        "phone",
        "is_active",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )


@admin.register(Department)
class DepartmentAdmin(ModelAdmin):
    list_display = (
        "name",
        "code",
        "head",
    )
    search_fields = ("name", "code")


@admin.register(StudentProfile)
class StudentProfileAdmin(ModelAdmin):
    list_display = (
        "student_id",
        "user",
        "department",
        "status",
    )
    list_filter = (
        "status",
        "department",
    )
    search_fields = (
        "student_id",
        "user__username",
        "user__first_name",
        "user__last_name",
    )


@admin.register(Instructor)
class InstructorAdmin(ModelAdmin):
    list_display = (
        "staff_id",
        "user",
        "department",
        "title",
    )
    search_fields = (
        "staff_id",
        "user__username",
    )


@admin.register(AcademicYear)
class AcademicYearAdmin(ModelAdmin):
    list_display = (
        "year_label",
        "start_date",
        "end_date",
        "is_current",
    )


@admin.register(Semester)
class SemesterAdmin(ModelAdmin):
    list_display = (
        "name",
        "academic_year",
        "is_current",
    )


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = (
        "course_code",
        "title",
        "department",
        "credit_hours",
    )
    search_fields = (
        "course_code",
        "title",
    )


@admin.register(CourseSection)
class CourseSectionAdmin(ModelAdmin):
    list_display = (
        "course",
        "section_code",
        "semester",
        "instructor",
        "room",
    )


@admin.register(Enrollment)
class EnrollmentAdmin(ModelAdmin):
    list_display = (
        "student",
        "course_section",
        "status",
        "enrollment_date",
    )


@admin.register(Grade)
class GradeAdmin(ModelAdmin):
    list_display = (
        "enrollment",
        "assessment_type",
        "score",
        "letter_grade",
    )


@admin.register(Attendance)
class AttendanceAdmin(ModelAdmin):
    list_display = (
        "enrollment",
        "date",
        "status",
    )


@admin.register(FeePayment)
class FeePaymentAdmin(ModelAdmin):
    list_display = (
        "student",
        "semester",
        "amount",
        "method",
        "date",
    )