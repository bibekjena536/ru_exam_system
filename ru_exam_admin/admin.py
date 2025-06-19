from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CostomUser,Teachers_info_add_teacher,TeacherAuth,Student_info_add_student,StudentAuth
# Register your models here.

class CostomUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserChangeForm
    model=CostomUser
    list_display=["username","email","is_staff","is_superuser"]


admin.site.register(CostomUser,CostomUserAdmin)

@admin.register(Teachers_info_add_teacher)


class Teachers_info_add_teacher(admin.ModelAdmin):
    list_display =Teachers_info_add_teacher.DisplayFields
    search_fields=Teachers_info_add_teacher.SearchablFields



@admin.register(TeacherAuth)
class TeacherAuthAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)
    
    
# Register the Student_info_add_student model with a custom admin class

# Register Student_info_add_student with custom admin class
@admin.register(Student_info_add_student)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = Student_info_add_student.DisplayFields  # Use the DisplayFields attribute
    search_fields = [
        'Student_info_add_student_f_name',
        'Student_info_add_student_l_name',
        'Student_info_add_student_email',
        'Student_info_add_student_exam_rollnumber'
    ]
    list_filter = [
        'Student_info_add_student_department',
        'Student_info_add_student_branch',
        'Student_info_add_student_gender'
    ]
    ordering = ['Student_info_add_student_serial_number']  # Order by serial number


# Register StudentAuth with custom admin class
@admin.register(StudentAuth)
class StudentAuthAdmin(admin.ModelAdmin):
    list_display = ('student', 'email', 'is_active', 'is_verified', 'created_at', 'updated_at')
    search_fields = ['email', 'student__Student_info_add_student_f_name', 'student__Student_info_add_student_l_name']
    list_filter = ['is_active', 'is_verified']
    ordering = ['created_at']  # Order by creation date