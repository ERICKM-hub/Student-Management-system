from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    class RoleChoices(models.TextChoices):
        LECTURER = "Lecturer", "Lecturer"
        STUDENT = "Student", "Student"
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField( max_length=20,choices=RoleChoices.choices,default=RoleChoices.STUDENT )
    location = models.CharField(max_length=150, default="Nairobi, Kenya")
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    def __str__(self):
        return self.username
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    head = models.ForeignKey( "Instructor", on_delete=models.SET_NULL,null=True,blank=True,related_name="headed_departments")
    def __str__(self):
        return f"{self.name} ({self.code})"
class Instructor(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="instructor_profile")
    staff_id = models.CharField(max_length=20, unique=True,default="LIT-02/2020")
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name="instructors")
    title = models.CharField(max_length=20, default="Prof.")
    hire_date = models.DateField()
    def __str__(self):
        return self.user.get_full_name() or self.user.username
class StudentProfile(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = "Active", "Active"
        SUSPENDED = "Suspended", "Suspended"
        GRADUATED = "Graduated", "Graduated"
        WITHDRAWN = "Withdrawn", "Withdrawn"
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="student_profile")
    student_id = models.CharField(max_length=20, unique=True,default="BCS-02-8574/2024")
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True, related_name="students"    )
    admission_date = models.DateField(auto_now_add=True)
    guardian_fullname = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20,choices=StatusChoices.choices,default=StatusChoices.ACTIVE)
    def __str__(self):
        return self.user.get_full_name() or self.user.username
class AcademicYear(models.Model):
    year_label = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    def __str__(self):
        return self.year_label
class Semester(models.Model):
    name = models.CharField(max_length=20)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE,related_name="semester")
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} ({self.academic_year})"
class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name="courses")
    credit_hours = models.PositiveSmallIntegerField()
    prerequisites = models.ManyToManyField("self",symmetrical=False,blank=True,related_name="required_for")
    def __str__(self):
        return f"{self.course_code} - {self.title}"
class CourseSection(models.Model):
    class SectionChoices(models.TextChoices):
        A = "A", "A"
        B = "B", "B"
        C = "C", "C"
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="sections")
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,related_name="course_sections")
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name="course_sections")
    section_code = models.CharField(max_length=5,choices=SectionChoices.choices,default=SectionChoices.A)
    capacity = models.PositiveIntegerField()
    schedule = models.DateTimeField()
    room = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.course} - {self.section_code}"
class Enrollment(models.Model):
    class StatusChoices(models.TextChoices):
        ENROLLED = "Enrolled", "Enrolled"
        DROPPED = "Dropped", "Dropped"
        COMPLETED = "Completed", "Completed"
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name="enrollments")
    course_section = models.ForeignKey( CourseSection,on_delete=models.CASCADE,related_name="enrollments")
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15,choices=StatusChoices.choices,default=StatusChoices.ENROLLED)
    def __str__(self):
        return f"{self.student} - {self.course_section}"
class Grade(models.Model):
    class AssessmentType(models.TextChoices):
        CAT = "CAT", "CAT"
        EXAM = "Exam", "Exam"
        ASSIGNMENT = "Assignment", "Assignment"
    enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE,related_name="grades")
    assessment_type = models.CharField(max_length=20,choices=AssessmentType.choices,default=AssessmentType.EXAM)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    letter_grade = models.CharField(max_length=2)
    date_recorded = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.letter_grade}"
class Attendance(models.Model):
    class StatusChoices(models.TextChoices):
        PRESENT = "Present", "Present"
        ABSENT = "Absent", "Absent"
        LATE = "Late", "Late"
        EXCUSED = "Excused", "Excused"
    enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE,related_name="attendance_records")
    date = models.DateField()
    status = models.CharField(max_length=10,choices=StatusChoices.choices,default=StatusChoices.ABSENT)
    def __str__(self):
        return f"{self.date} - {self.status}"
class FeePayment(models.Model):
    class PaymentMethod(models.TextChoices):
        MPESA = "Mpesa", "Mpesa"
        CASH = "Cash", "Cash"
        BANK = "Bank", "Bank"
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name="fee_payments")
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,related_name="fee_payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    method = models.CharField( max_length=20,choices=PaymentMethod.choices, default=PaymentMethod.MPESA)
    reference_number = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return f"{self.student} - KES {self.amount}"