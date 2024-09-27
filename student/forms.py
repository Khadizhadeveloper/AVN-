from django import forms

from student.models import Student, Grade, Subject


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email', 'help_text': 'A valid email address'})
    )
    student_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Student Number'})
    )

    class Meta:
        model = Student
        fields = '__all__'

class GradeForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields=['grade']
        widgets={
            'grade': forms.NumberInput(attrs={'placeholder': 'Введите оценку', 'min': 0, 'max': 100}),
        }


