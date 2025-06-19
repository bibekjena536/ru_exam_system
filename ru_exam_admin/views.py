from django.shortcuts import render

# Create your views here.
from unittest import loader
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import (CostomUser,TeacherManager,
                     Teachers_info_add_teacher,TeacherAuth,
                     StudentAuth,Student_info_add_student)
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail



def admin_home(request):
    if request.user.is_authenticated:
        admin_email = request.user.email
        Admin_data = CostomUser.objects.filter(email=admin_email).only()
        # Pass the context data to the template using `render`
        return render(request, "admin_pannel/admin_pannel.html", {'Admin_data': Admin_data})
    else:
        return render(request, "admin_pannel/root_admin_index.html")



def index(request):
    if request.user.is_authenticated:
        admin_email = request.user.email
        Admin_data = CostomUser.objects.filter(email=admin_email).only()
        # Pass the context data to the template using `render`
        return render(request, "admin_pannel/admin_pannel.html", {'Admin_data': Admin_data})
    else:
        return render(request, "admin_pannel/index.html")
    
    
    



def admin_signin_root(request):
    if request.method == 'POST':
        username = request.POST.get('Admin_email_super')
        password = request.POST.get('Admin_password_super')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_home')  # Redirect to the admin_home view
        else:
            return HttpResponse('Incorrect username or password!!, go back and login again')

    return render(request, "admin_pannel/root_admin_index.html")


def admin_model_create_teacher(request):
    if request.method == 'POST':
        email = request.POST.get('staff_member_email')
        first_name = request.POST.get('staff_member_first_name')
        last_name = request.POST.get('staff_member_last_name')
        password = request.POST.get('staff_member_confirm_password')
        
        
        # Store on teachers database
        
        Teachers_info_add_teacher_honorifics=request.POST.get('honorifics_of_staff')
        Teachers_info_add_teacher_f_name=request.POST.get('staff_member_first_name')
        Teachers_info_add_teacher_username=request.POST.get('staff_member_email')
        Teachers_info_add_teacher_l_name=request.POST.get('staff_member_last_name')
        
        Teachers_info_add_teacher_email=request.POST.get('staff_member_email')
        Teachers_info_add_teacher_phoneno=request.POST.get('staff_member_phone')
        Teachers_info_add_teacher_password= request.POST.get('staff_member_confirm_password')
        Teachers_info_add_teacher_designation= request.POST.get('staff_member_designation')
        Teachers_info_add_teacher_department= request.POST.get('staff_member_department')
        
        

        # Check if email already exists
        if TeacherAuth.objects.filter(email=email).exists():
            messages.error(request, 'A teacher with this email already exists.')
            return redirect('admin_add_staff')
        
        user=Teachers_info_add_teacher(Teachers_info_add_teacher_honorifics=Teachers_info_add_teacher_honorifics,
                      Teachers_info_add_teacher_f_name=Teachers_info_add_teacher_f_name,
                      Teachers_info_add_teacher_username=Teachers_info_add_teacher_username,
                      Teachers_info_add_teacher_email=Teachers_info_add_teacher_email,
                      Teachers_info_add_teacher_l_name=Teachers_info_add_teacher_l_name,
                      Teachers_info_add_teacher_phoneno=Teachers_info_add_teacher_phoneno,
                      Teachers_info_add_teacher_password=Teachers_info_add_teacher_password,
                      Teachers_info_add_teacher_designation=Teachers_info_add_teacher_designation,
                      Teachers_info_add_teacher_department=Teachers_info_add_teacher_department,
                      )
        user.save()

        # Create the teacher user
        teacher = TeacherAuth.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        send_mail(
             subject='Registration Successful',
             message=f'Hello,{user.Teachers_info_add_teacher_honorifics} {teacher.first_name},your password:- {password} . Your email is {user.Teachers_info_add_teacher_email}, Thank you for registering.',
             
             from_email='ruexamsystem@gmail.com',  # Replace with your email
             recipient_list=[teacher.email],
             fail_silently=False,
                )

        messages.success(request, f'Teacher {teacher.first_name} {teacher.last_name} created successfully!')
        return redirect('admin_add_staff')

    return render(request, 'admin_pannel/add_staff.html')




'''def admin_model_create_student(request):
    if request.method == 'POST':
        email = request.POST.get('reg_admin_student_email')
        password = request.POST.get('reg_admin_student_password')
        
        
        # Store on teachers database
        
        #Student_info_add_student_serial_number=request.POST.get('')
        Student_info_add_student_f_name=request.POST.get('reg_admin_student_first_name')
        Student_info_add_student_l_name=request.POST.get('reg_admin_student_last_name')
        Student_info_add_student_father_name=request.POST.get('reg_admin_student_father_name')
        Student_info_add_student_mother_name=request.POST.get('reg_admin_student_mother_name')
        Student_info_add_student_college_ro=request.POST.get('reg_admin_student_roll_no')
        Student_info_add_student_gender=request.POST.get('reg_admin_student_gender')
        Student_info_add_student_email=request.POST.get('reg_admin_student_email')
        Student_info_add_student_username=request.POST.get('reg_admin_student_email')
        Student_info_add_student_DoB=request.POST.get('reg_admin_student_dob')
        Student_info_add_student_phoneno=request.POST.get('reg_admin_student_contact_number')
        Student_info_add_student_adress=request.POST.get('reg_admin_student_address')
        Student_info_add_student_categori=request.POST.get('reg_admin_student_category')
        Student_info_add_student_Disable_status=request.POST.get('reg_admin_student_disability_status')
        Student_info_add_student_password=request.POST.get('reg_admin_student_password')
        Student_info_add_student_department=request.POST.get('reg_admin_student_department')
        Student_info_add_student_branch=request.POST.get('reg_admin_student_branch')
        Student_info_add_student_photo=request.POST.get('reg_admin_student_photo')
        Student_info_add_student_sign=request.POST.get('reg_admin_student_signature')
        Student_info_add_student_idproof=request.POST.get('reg_admin_student_id_proof')
        #Student_info_add_student_joindate=request.POST.get('')
        #Student_info_add_student_exam_rollnumber=request.POST.get('')
        
        
        

        # Check if email already exists
        if StudentAuth.objects.filter(email=email).exists():
            messages.error(request, 'A Student with this email already exists.')
            return redirect('admin_add_staff')
        
        user=Student_info_add_student(Student_info_add_student_f_name=Student_info_add_student_f_name,
                                      Student_info_add_student_l_name=Student_info_add_student_l_name,
                                      Student_info_add_student_father_name=Student_info_add_student_father_name,
                                      Student_info_add_student_mother_name=Student_info_add_student_mother_name,
                                      Student_info_add_student_college_ro=Student_info_add_student_college_ro,
                                      Student_info_add_student_gender=Student_info_add_student_gender,
                                      Student_info_add_student_email=Student_info_add_student_email,
                                      Student_info_add_student_username=Student_info_add_student_username,
                                      Student_info_add_student_DoB=Student_info_add_student_DoB,
                                      Student_info_add_student_phoneno=Student_info_add_student_phoneno,
                                      Student_info_add_student_adress=Student_info_add_student_adress,
                                      Student_info_add_student_categori=Student_info_add_student_categori,
                                      Student_info_add_student_Disable_status=Student_info_add_student_Disable_status,
                                      Student_info_add_student_password=Student_info_add_student_password,
                                      Student_info_add_student_department=Student_info_add_student_department,
                                      Student_info_add_student_branch=Student_info_add_student_branch,
                                      Student_info_add_student_photo=Student_info_add_student_photo,
                                      Student_info_add_student_sign=Student_info_add_student_sign,
                                      Student_info_add_student_idproof=Student_info_add_student_idproof,
                                      #Student_info_add_student_joindate=Student_info_add_student_joindate,
                                      #Student_info_add_student_exam_rollnumber=Student_info_add_student_exam_rollnumber, 
                                        
                                      
                                      )
        user.save()

        # Create the teacher user
        student = StudentAuth.objects.create(
            email=email,
            password=password,
        )
        return redirect('admin_add_student')

    return render(request, 'admin_pannel/add_student.html')'''
    
def admin_model_create_student(request):
    if request.method == 'POST':
        email = request.POST.get('reg_admin_student_email')
        password = request.POST.get('reg_admin_student_password')

        # Extract student data from the form
        student_data = {
            "Student_info_add_student_f_name": request.POST.get('reg_admin_student_first_name'),
            "Student_info_add_student_l_name": request.POST.get('reg_admin_student_last_name'),
            "Student_info_add_student_father_name": request.POST.get('reg_admin_student_father_name'),
            "Student_info_add_student_mother_name": request.POST.get('reg_admin_student_mother_name'),
            "Student_info_add_student_college_ro": request.POST.get('reg_admin_student_roll_no'),
            "Student_info_add_student_gender": request.POST.get('reg_admin_student_gender'),
            "Student_info_add_student_email": email,
            "Student_info_add_student_username": email,
            "Student_info_add_student_DoB": request.POST.get('reg_admin_student_dob'),
            "Student_info_add_student_phoneno": request.POST.get('reg_admin_student_contact_number'),
            "Student_info_add_student_adress": request.POST.get('reg_admin_student_address'),
            "Student_info_add_student_categori": request.POST.get('reg_admin_student_category'),
            "Student_info_add_student_Disable_status": request.POST.get('reg_admin_student_disability_status'),
            "Student_info_add_student_password": password,
            "Student_info_add_student_department": request.POST.get('reg_admin_student_department'),
            "Student_info_add_student_branch": request.POST.get('reg_admin_student_branch'),
            "Student_info_add_student_photo": request.FILES.get('reg_admin_student_photo'),
            "Student_info_add_student_sign": request.FILES.get('reg_admin_student_signature'),
            "Student_info_add_student_idproof": request.FILES.get('reg_admin_student_id_proof'),
        }

        # Check if email already exists
        if StudentAuth.objects.filter(email=email).exists():
            messages.error(request, 'A Student with this email already exists.')
            return redirect('admin_add_student')

        # Create the Student_info_add_student instance
        student = Student_info_add_student.objects.create(**student_data)

        # Create the StudentAuth instance and link it to the student
        StudentAuth.objects.create(
            student=student,  # Link the Student_info_add_student instance
            email=email,
            password=password,
        )

        messages.success(request, f'Student {student.Student_info_add_student_f_name} {student.Student_info_add_student_l_name} created successfully!')
        return redirect('admin_add_student')

    return render(request, 'admin_pannel/add_student.html')

@login_required(login_url="admin_home")
def admin_add_student(request):
    if request.user.is_authenticated:
        admin_email = request.user.email
        Admin_data=CostomUser.objects.filter(email=admin_email).only()
        
        
        return render(request,"admin_pannel/add_student.html",{'Admin_data':Admin_data,})
        
    else:
        return render(request,"admin_pannel/root_admin_index.html")
    
    return render(request,"admin_pannel/add_student.html")


@login_required(login_url="admin_home")
def admin_admin_pannel(request):
    if request.user.is_authenticated:
        admin_email = request.user.email
        Admin_data=CostomUser.objects.filter(email=admin_email).only()
        
        
        return render(request,"admin_pannel/admin_pannel.html",{'Admin_data':Admin_data,})
        
    else:
        return render(request,"admin_pannel/root_admin_index.html")
    
    return render(request,"admin_pannel/admin_pannel.html")



@login_required(login_url="admin_home")
def admin_add_staff(request):
    
    
    return render(request,"admin_pannel/add_staff.html")




@login_required(login_url="admin_home")
def admin_view_staff(request):
    
    admin_staff_dada_view=Teachers_info_add_teacher.objects.all().order_by('Teachers_info_add_teacher_serial_number')
    if request.method == 'GET':
        filterstaff_admin=request.GET.get('serchbox_viewstaff_admin')
        # Validate the input
        if filterstaff_admin:
            if filterstaff_admin.isdigit():  # Check if the input is numeric
                admin_staff_dada_view = Teachers_info_add_teacher.objects.filter(
                    Teachers_info_add_teacher_serial_number=filterstaff_admin
                )
            else:
                # If the input is not numeric, filter by other fields (e.g., name, email, etc.)
                admin_staff_dada_view = Teachers_info_add_teacher.objects.filter(
                    Teachers_info_add_teacher_f_name__icontains=filterstaff_admin
                ) | Teachers_info_add_teacher.objects.filter(
                    Teachers_info_add_teacher_l_name__icontains=filterstaff_admin
                ) | Teachers_info_add_teacher.objects.filter(
                    Teachers_info_add_teacher_email__icontains=filterstaff_admin
                )
        
        
        
        
        
    '''for a in admin_staff_dada_view:  #test for fatch data from table
        print(a.Teachers_info_add_teacher_serial_number)       # - for change the order of data in staff view page
        print(a.Teachers_info_add_teacher_f_name)
        print(a.Teachers_info_add_teacher_username)
        print(a.Teachers_info_add_teacher_l_name)
        print(a.Teachers_info_add_teacher_email)
        print(a.Teachers_info_add_teacher_phoneno)
        print(a.Teachers_info_add_teacher_password)
        print(a.Teachers_info_add_teacher_joindate)
        print(a.Teachers_info_add_teacher_designation)
        print(a.Teachers_info_add_teacher_department)'''
    admin_all_staff_data={
        'admin_staff_dada_view':admin_staff_dada_view
    }
    
    return render(request,"admin_pannel/view_staff.html",admin_all_staff_data)





@login_required(login_url="admin_home")
def admin_view_student(request):

    
    admin_student_dada_view=Student_info_add_student.objects.all().order_by('Student_info_add_student_serial_number')
    if request.method == 'GET':
        filterstudent_admin=request.GET.get('student_search')
        # Validate the input
        if filterstudent_admin:
            if filterstudent_admin.isdigit():  # Check if the input is numeric
                admin_student_dada_view = Student_info_add_student.objects.filter(
                    Student_info_add_student_exam_rollnumber=filterstudent_admin
                )
            else:
                # If the input is not numeric, filter by other fields (e.g., name, email, etc.)
                admin_student_dada_view = Student_info_add_student.objects.filter(
                    Student_info_add_student_f_name__icontains=filterstudent_admin
                ) | Student_info_add_student.objects.filter(
                    Student_info_add_student_department__icontains=filterstudent_admin
                ) | Student_info_add_student.objects.filter(
                    Student_info_add_student_email__icontains=filterstudent_admin
                )
        
        
    admin_all_student_dada_view={
        'admin_student_dada_view':admin_student_dada_view
    }
    
    return render(request,"admin_pannel/view_student.html",admin_all_student_dada_view)

    
    return render(request,"admin_pannel/view_student.html")




@login_required(login_url="admin_home")
def admin_manage_exam(request):
    
    
    return render(request,"admin_pannel/manage_exam.html")

@login_required(login_url="admin_home")
def admin_manageexam_upcomming_exam(request):
    
    
    return render(request,"admin_pannel/upcomming_exam.html")


@login_required(login_url="admin_home")
def admin_manageexam_check_students_system(request):
    
    
    return render(request,"admin_pannel/check_students_system.html")


@login_required(login_url="admin_home")
def admin_exam_send_notice(request):
    
    
    return render(request,"admin_pannel/send_notice.html")



@login_required(login_url="admin_home")
def admin_check_questions(request):
    
    
    return render(request,"admin_pannel/check_questions.html")


@login_required(login_url="admin_home")
def admin_result_view(request):
    
    
    return render(request,"admin_pannel/result_view.html")



@login_required(login_url="admin_home")
def admin_feedback_view(request):
    
    
    return render(request,"admin_pannel/feedback_view.html")



@login_required(login_url="admin_home")
def admin_contact_us(request):
    
    
    return render(request,"admin_pannel/contact_us.html")



@login_required(login_url="admin_home")
def admin_create_exam(request):
    
    admin_teacher_dada_view=Teachers_info_add_teacher.objects.all()
    admin_teacher_dada={
        'admin_teacher_dada_view':admin_teacher_dada_view
    }
    
    return render(request,"admin_pannel/create_exam.html",admin_teacher_dada)



@login_required(login_url="admin_home")
def admin_upcomming_exam(request):
    
    
    return render(request,"admin_pannel/upcomming_exam.html")


@login_required(login_url="admin_home")
def admin_manage_papers(request):
    
    
    return render(request,"admin_pannel/manage_papers.html")



@login_required(login_url="admin_home")
def admin_send_notice(request):
    
    
    return render(request,"admin_pannel/send_notice.html")




@login_required(login_url="admin_home")
def delete_teacher(request, email):
    if request.method == 'POST':
        # Get the teacher object by email or return a 404 if not found
        teacher = get_object_or_404(Teachers_info_add_teacher, Teachers_info_add_teacher_email=email)
        teacher = get_object_or_404(Teachers_info_add_teacher, Teachers_info_add_teacher_email=email)
        teacher.delete()  # Delete the teacher from the Teachers_info_add_teacher
        teacher_user = TeacherAuth.objects.filter(email=email).first()
        if teacher_user:
            teacher_user.delete()# delete the teacher from the TeacherAuth model
        # Optionally, you can also delete the user from the TeacherAuth model

        messages.success(request, f'Teacher with email {email} has been deleted successfully!')
        return redirect('admin_view_staff')  # Redirect to the staff view page



@login_required(login_url="admin_home")
def delete_student(request, email):
    if request.method == 'GET':
        # Get the student object by email or return a 404 if not found
        student = get_object_or_404(Student_info_add_student, Student_info_add_student_email=email)
        student = get_object_or_404(Student_info_add_student, Student_info_add_student_email=email)
        student.delete()  # Delete the teacher from the Teachers_info_add_teacher
        student_user = StudentAuth.objects.filter(email=email).first()
        if student_user:
            student_user.delete()# delete the teacher from the TeacherAuth model
        # Optionally, you can also delete the user from the TeacherAuth model

        messages.success(request, f'Student with email {email} has been deleted successfully!')
        return redirect('admin_view_student')  # Redirect to the staff view page



@login_required(login_url="admin_home")
def view_studentdetail(request, email):
    
    admin_student_dada_feltred = Student_info_add_student.objects.filter(
                    Student_info_add_student_email=email
                ).only()
    return render(request,"admin_pannel/view_student_detail.html",{'admin_student_dada_feltred':admin_student_dada_feltred,})






@login_required(login_url="admin_home")
def update_teacher(request, email):
    if request.method == 'POST':
        
        # Get the teacher object by email or return a 404 if not found
        teacher_info = get_object_or_404(Teachers_info_add_teacher, Teachers_info_add_teacher_email=email)
        teacher_user = get_object_or_404(TeacherAuth, email=email)

        # Get updated data from the form
        honorifics = request.POST.get('update_honorifics')
        first_name = request.POST.get('update_teacher_first_name')
        last_name = request.POST.get('update_teacher_last_name')
        phone = request.POST.get('update_teacher_phone')
        department = request.POST.get('update_department')
        designation = request.POST.get('update_designation')

        # Update Teachers_info_add_teacher table
        teacher_info.Teachers_info_add_teacher_honorifics = honorifics
        teacher_info.Teachers_info_add_teacher_f_name = first_name
        teacher_info.Teachers_info_add_teacher_l_name = last_name
        teacher_info.Teachers_info_add_teacher_phoneno = phone
        teacher_info.Teachers_info_add_teacher_department = department
        teacher_info.Teachers_info_add_teacher_designation = designation
        teacher_info.save()
        
        # Update TeacherAuth table
        teacher_user.first_name = first_name
        teacher_user.last_name = last_name
        teacher_user.save()

        # Success message and redirect
        messages.success(request, f'Teacher with email {email} has been updated successfully!')
        return redirect('admin_view_staff')  # Redirect to the staff view page






def signout(request):
    logout(request)
    return render(request,"admin_pannel/root_admin_index.html")