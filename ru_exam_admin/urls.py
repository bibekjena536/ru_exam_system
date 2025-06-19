"""
URL configuration for ru_exam_system project.

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
from ru_exam_admin import views
from ru_exam_system import settings
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_teacher,update_teacher,delete_student,view_studentdetail

urlpatterns = [
    path('admin_root_database', admin.site.urls),
    
    path('delete-teacher/<str:email>/', delete_teacher, name='delete_teacher'),
    
    path('delete-student/<str:email>/', delete_student, name='delete_student'),
    
    path('update-teacher/<str:email>/', update_teacher, name='update_teacher'),
    
    path('view-studentdetail/<str:email>/', view_studentdetail, name='view_studentdetail'),
    
    path('admin_home',views.admin_home,name="admin_home"),
    
    
    path('admin_admin_pannel',views.admin_admin_pannel,name="admin_admin_pannel"),
    
    path('admin_add_staff',views.admin_add_staff,name="admin_add_staff"),
    
    path('admin_view_staff',views.admin_view_staff,name="admin_view_staff"),
    
    path('admin_add_student',views.admin_add_student,name="admin_add_student"),
    
    path('admin_view_student',views.admin_view_student,name="admin_view_student"),
    
    #path('admin_view_student_detail',views.admin_view_student_detail,name="admin_view_student_detail"),
    
    path('admin_manage_exam',views.admin_manage_exam,name="admin_manage_exam"),
    
    path('admin_create_exam',views.admin_create_exam,name="admin_create_exam"),
    
    path('admin_upcomming_exam',views.admin_upcomming_exam,name="admin_upcomming_exam"),
    
    path('admin_manage_papers',views.admin_manage_papers,name="admin_manage_papers"),
    
    path('admin_send_notice',views.admin_send_notice,name="admin_send_notice"),
    
    path('admin_manageexam_check_students_system',views.admin_manageexam_check_students_system,name="admin_manageexam_check_students_system"),
    
    path('admin_manageexam_upcomming_exam',views.admin_manageexam_upcomming_exam,name="admin_manageexam_upcomming_exam"),
   
    path('admin_exam_send_notice',views.admin_exam_send_notice,name="admin_exam_send_notice"),
    
    path('admin_check_questions',views.admin_check_questions,name="admin_check_questions"),
    
    path('admin_result_view',views.admin_result_view,name="admin_result_view"),
    
    path('admin_contact_us',views.admin_contact_us,name="admin_contact_us"),
    
    path('admin_feedback_view',views.admin_feedback_view,name="admin_feedback_view"),
    
    path('admin_signin_root',views.admin_signin_root,name="admin_signin_root"),
    
    path('admin_model_create_teacher',views.admin_model_create_teacher,name="admin_model_create_teacher"),
    
    path('admin_model_create_student',views.admin_model_create_student,name="admin_model_create_student"),
    
    #path('save_teacher_data',views.save_teacher_data,name="save_teacher_data"),
    path('signout',views.signout,name="signout"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
