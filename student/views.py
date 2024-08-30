from functools import reduce

from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
# Create your views here.
def create_student(request):
    if request.method == 'POST':
        form=StudentForm(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          return redirect('home')

    else:
        form=StudentForm()
        return render(request, 'student/create_student.html', {'form':form})


def all_students(request):
    students = Student.objects.order_by('-id')
    return render(request, 'student/index.html', {'students': students})




def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = StudentForm(instance=student)
        return render(request, 'student/edit_student.html', { 'student':student, 'form':form,})


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    messages.success('Deleted succesfully!', messages.SUCCESS)
    return redirect('/home')






