from rest_framework import serializers
from .models import *

class userProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
            'location',
            'is_active',
            'is_superuser',
        ]

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id',
            'name',
            'code',
            'description',
            'head',
        ]

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = [
            'id',
            'user',
            'staff_id',
            'department',
            'title',
            'hire_date',
        ]

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = [
            'id',
            'user',
            'student_id',
            'department',
            'admission_date',
            'guardian_fullname',
            'guardian_phone',
            'status',
        ]

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = [
            'id',
            'year_label',
            'start_date',
            'end_date',
            'is_current',
        ]

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = [
            'id',
            'name',
            'academic_year',
            'start_date',
            'end_date',
            'is_current',
        ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'course_code',
            'title',
            'description',
            'department',
            'credit_hours',
            'prerequisites',
        ]

class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = [
            'id',
            'course',
            'semester',
            'instructor',
            'section_code',
            'capacity',
            'schedule',
            'room',
        ]

class EnrollmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            'id',
            'student',
            'course_section',
            'enrollment_date',
            'status',
        ]

class GradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = [
            'id',
            'enrollment',
            'assessment_type',
            'score',
            'max_score',
            'weight',
            'letter_grade',
            'date_recorded',
        ]

class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [
            'id',
            'enrollment',
            'date',
            'status',
        ]

class FeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePayment
        fields = [
            'id',
            'student',
            'semester',
            'amount',
            'date',
            'method',
            'reference_number',
        ]