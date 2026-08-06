from django.shortcuts import render , get_object_or_404
from .forms import StudentForm
from .models import Student

def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    return render(request , 'student_create.html', {'form' : form})

def student_list(request):
    Students = Student.objects.all()
    return render(request , 'student_list.html' , {'students' : Students})

def student_detail(request , pk):
    student = get_object_or_404(Student , pk=pk)
    return render(request,'student_detail.html' , {'student' : student})