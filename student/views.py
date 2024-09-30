from email.policy import default

from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View
from .models import Student, Grade, Subject
from .forms import StudentForm, GradeForm


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/create_student.html'

    def form_valid(self, form):
        student=form.save(commit=False)
        student.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student:home')



class StudentListView(ListView):
    model = Student
    template_name = 'student/index.html'
    context_object_name = 'students'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['student']=self.get_queryset()
        return context




class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/edit_student.html'
    form_class = StudentForm
    success_url = reverse_lazy('student:home')

    def get_success_url(self):
        return reverse_lazy('student:home')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail_student.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grades']=Grade.objects.filter(student=self.object)
        return context




class AssignGradeView(View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        subjects=Subject.objects.all()
        for index, subject in enumerate(subjects, start=1):
            grade_value=request.POST.get(f'grade_{subject.id}')
            if grade_value:
                Grade.objects.update_or_create(
                    student=student,
                    subject=subject,
                    defaults={'grade': grade_value}
                )
        return redirect('student:student-detail', pk=student_id)

class EditGradesView(View):
    GradeFormset = modelformset_factory(Grade, fields=('subject', 'grade'), extra=0)

    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        grades = Grade.objects.filter(student=student)
        formset = self.GradeFormset(queryset=grades)
        return render(request, 'student/edit_grades.html', {'formset': formset, 'student': student})

    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        grades = Grade.objects.filter(student=student)
        formset = self.GradeFormset(request.POST, queryset=grades)
        if formset.is_valid():
            formset.save()
            return redirect('student:student-detail', pk=student.id)
        else:
            print(formset.errors)
        return render(request, 'student/edit_grades.html', {'formset': formset, 'student': student})



def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student:home')

