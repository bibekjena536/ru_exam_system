from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
import random
import os
from datetime import datetime

from django.db import models

# Create your models here.

class CostomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=("username",)
    
    def __str__(self):
        return self.username
  
  
  #Teachers information table 
class Teachers_info_add_teacher(models.Model):
    
    
    Teachers_info_add_teacher_serial_number = models.AutoField(primary_key=True)
    Teachers_info_add_teacher_honorifics=models.CharField(max_length=150)
    Teachers_info_add_teacher_f_name=models.CharField(max_length=150)
    Teachers_info_add_teacher_username=models.CharField(max_length=150)
    Teachers_info_add_teacher_l_name=models.CharField(max_length=150)
    Teachers_info_add_teacher_email=models.EmailField(max_length=150)
    Teachers_info_add_teacher_phoneno=models.CharField(max_length=150)
    Teachers_info_add_teacher_password=models.CharField(max_length=150)
    Teachers_info_add_teacher_designation=models.CharField(max_length=150)
    Teachers_info_add_teacher_department=models.CharField(max_length=150)
    #STeachers_info_add_teacher_gender=models.CharField(max_length=150)
    
    #Teachers_info_add_teacher_DoB=models.DateField(auto_now=False, auto_now_add=False,)
    Teachers_info_add_teacher_joindate = models.DateTimeField(auto_now_add=True)
    DisplayFields = ['Teachers_info_add_teacher_serial_number',
        'Teachers_info_add_teacher_f_name', 'Teachers_info_add_teacher_username',
        'Teachers_info_add_teacher_l_name', 'Teachers_info_add_teacher_email',
        'Teachers_info_add_teacher_phoneno', 'Teachers_info_add_teacher_password',
        'Teachers_info_add_teacher_joindate', 'Teachers_info_add_teacher_designation',
        'Teachers_info_add_teacher_department', 'Teachers_info_add_teacher_honorifics'
    ]
    SearchablFields=['Teachers_info_add_teacher_f_name','Teachers_info_add_teacher_username']
    def __str__(self):
        return self.Teachers_info_add_teacher_username






 




# Custom Manager for TeacherAuth
# Custom Manager for TeacherAuth
class TeacherManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        teacher = self.model(email=email, **extra_fields)
        teacher.set_password(password)
        teacher.save(using=self._db)
        return teacher

# TeacherAuth Model
class TeacherAuth(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access
    is_superuser = models.BooleanField(default=False)  # Required for superuser access

    # Avoid conflicts with CostomUser by adding related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='teacher_auth_users',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='teacher_auth_users',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = TeacherManager()  # Use the custom manager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True
    
    
    
    
    
    
    
    
  #Student information table
  
  
def student_photo_upload_path(instance, filename):
    """
    Custom upload path for student photos.
    Renames the file to a specific pattern: student_photo_<exam_rollnumber>.<extension>
    """
    ext = filename.split('.')[-1]
    new_filename = f"student_photo_{instance.Student_info_add_student_exam_rollnumber}.{ext}"
    return os.path.join('student_reg_pics', new_filename)

def student_sign_upload_path(instance, filename):
    """
    Custom upload path for student signatures.
    Renames the file to a specific pattern: student_sign_<exam_rollnumber>.<extension>
    """
    ext = filename.split('.')[-1]
    new_filename = f"student_sign_{instance.Student_info_add_student_exam_rollnumber}.{ext}"
    return os.path.join('student_reg_sign', new_filename)

def student_idproof_upload_path(instance, filename):
    """
    Custom upload path for student ID proofs.
    Renames the file to a specific pattern: student_idproof_<exam_rollnumber>.<extension>
    """
    ext = filename.split('.')[-1]
    new_filename = f"student_idproof_{instance.Student_info_add_student_exam_rollnumber}.{ext}"
    return os.path.join('student_reg_document_idproof', new_filename)
 
class Student_info_add_student(models.Model):
    Student_info_add_student_serial_number = models.AutoField(primary_key=True)
    Student_info_add_student_f_name = models.CharField(max_length=150)
    Student_info_add_student_l_name = models.CharField(max_length=150)
    Student_info_add_student_father_name = models.CharField(max_length=150)
    Student_info_add_student_mother_name = models.CharField(max_length=150)
    Student_info_add_student_college_ro = models.CharField(max_length=150)
    Student_info_add_student_gender = models.CharField(max_length=150)
    Student_info_add_student_email = models.EmailField(max_length=150)
    Student_info_add_student_username = models.CharField(max_length=150)
    Student_info_add_student_DoB = models.DateField(auto_now=False, auto_now_add=False)
    Student_info_add_student_phoneno = models.CharField(max_length=150)
    Student_info_add_student_adress = models.CharField(max_length=400)
    Student_info_add_student_categori = models.CharField(max_length=150)
    Student_info_add_student_Disable_status = models.CharField(max_length=150)
    Student_info_add_student_password = models.CharField(max_length=150)
    Student_info_add_student_department = models.CharField(max_length=150)
    Student_info_add_student_branch = models.CharField(max_length=150)
    Student_info_add_student_photo = models.ImageField(
        max_length=300,
        upload_to=student_photo_upload_path
    )
    Student_info_add_student_sign = models.ImageField(
        max_length=300,
        upload_to=student_sign_upload_path
    )
    Student_info_add_student_idproof = models.FileField(
        max_length=300,
        upload_to=student_idproof_upload_path
    )
    Student_info_add_student_joindate = models.DateTimeField(auto_now_add=True)
    Student_info_add_student_exam_rollnumber = models.CharField(
        max_length=8,
        unique=True,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.Student_info_add_student_username

    def save(self, *args, **kwargs):
        # Generate a unique roll number if it doesn't exist
        if not self.Student_info_add_student_exam_rollnumber:
            self.Student_info_add_student_exam_rollnumber = self.generate_rollnumber()
        super().save(*args, **kwargs)

    def generate_rollnumber(self):
        # Use the current date and time instead of the join date
        now = datetime.now()
        year_month = now.strftime('%y%m')  # Format: YYMM

        # Count the number of students registered in the same year and month
        count = Student_info_add_student.objects.filter(
            Student_info_add_student_joindate__year=now.year,
            Student_info_add_student_joindate__month=now.month
        ).count() + 1  # Increment by 1 for the current student

        # Generate the roll number by combining year, month, and count
        rollnumber = f"{year_month}{count:04d}"  # Format: YYMMXXXX (8 digits)
        return rollnumber
    
    
    '''Student_info_add_student_serial_number = models.AutoField(primary_key=True)
    Student_info_add_student_f_name=models.CharField(max_length=150)
    Student_info_add_student_l_name=models.CharField(max_length=150)
    Student_info_add_student_father_name=models.CharField(max_length=150)
    Student_info_add_student_mother_name=models.CharField(max_length=150)
    Student_info_add_student_college_ro=models.CharField(max_length=150)
    Student_info_add_student_gender=models.CharField(max_length=150)
    Student_info_add_student_email=models.EmailField(max_length=150)
    Student_info_add_student_username=models.CharField(max_length=150)
    Student_info_add_student_DoB=models.DateField(auto_now=False, auto_now_add=False,)
    Student_info_add_student_phoneno=models.CharField(max_length=150)
    Student_info_add_student_adress=models.CharField(max_length=400)
    Student_info_add_student_categori=models.CharField(max_length=150)
    Student_info_add_student_Disable_status=models.CharField(max_length=150)
    Student_info_add_student_password=models.CharField(max_length=150)
    Student_info_add_student_department=models.CharField(max_length=150)
    Student_info_add_student_branch=models.CharField(max_length=150)
    Student_info_add_student_photo=models.ImageField(max_length=300,upload_to='student_reg_pics')
    Student_info_add_student_sign=models.ImageField(max_length=300,upload_to='student_reg_sign')
    Student_info_add_student_idproof=models.FileField(max_length=300,upload_to='student_reg_document_idproof')
    Student_info_add_student_joindate = models.DateTimeField(auto_now_add=True)
    Student_info_add_student_exam_rollnumber = models.CharField(
        max_length=8,
        unique=True,
        editable=False,  # Prevent manual editing
        null=True,  # Allow null values initially
        blank=True,  # Allow blank values in forms
    )'''
    
    DisplayFields = [
        'Student_info_add_student_serial_number',
        'Student_info_add_student_f_name',
        'Student_info_add_student_l_name',
        'Student_info_add_student_father_name',
        'Student_info_add_student_mother_name',
        'Student_info_add_student_college_ro',
        'Student_info_add_student_gender',
        'Student_info_add_student_email',
        'Student_info_add_student_username',
        'Student_info_add_student_DoB',
        'Student_info_add_student_phoneno',
        'Student_info_add_student_adress',
        'Student_info_add_student_categori',
        'Student_info_add_student_Disable_status',
        'Student_info_add_student_password',
        'Student_info_add_student_department',
        'Student_info_add_student_branch',
        'Student_info_add_student_photo',
        'Student_info_add_student_sign',
        'Student_info_add_student_idproof',
        'Student_info_add_student_joindate',
        'Student_info_add_student_exam_rollnumber'
    ]
    SearchablFields=['Student_info_add_student_f_name','Student_info_add_student_username']
    def __str__(self):
        return self.Student_info_add_student_username

    def save(self, *args, **kwargs):
        # Generate a unique roll number if it doesn't exist
        if not self.Student_info_add_student_exam_rollnumber:
            self.Student_info_add_student_exam_rollnumber = self.generate_rollnumber()
        super().save(*args, **kwargs)

    def generate_rollnumber(self):
        # Use the current date and time instead of the join date
        now = datetime.now()
        year_month = now.strftime('%y%m')  # Format: YYMM

        # Count the number of students registered in the same year and month
        count = Student_info_add_student.objects.filter(
            Student_info_add_student_joindate__year=now.year,
            Student_info_add_student_joindate__month=now.month
        ).count() + 1  # Increment by 1 for the current student

        # Generate the roll number by combining year, month, and count
        rollnumber = f"{year_month}{count:04d}"  # Format: YYMMXXXX (8 digits)
        return rollnumber

    
class StudentAuth(models.Model):
    student = models.OneToOneField(
        Student_info_add_student,
        on_delete=models.CASCADE,
        related_name='auth_info'
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)  # Indicates if the account is active
    is_verified = models.BooleanField(default=True)  # Indicates if the email is verified
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Auth Info for {self.student.Student_info_add_student_username}"
    
    
    