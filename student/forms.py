from django import forms

from student.models import Student


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Last Name'}))
    age=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Age'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': 'Email',
        'help_text':'A valid email address'}))
    student_number= forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Student Number'}))
    gender=forms.CharField(widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Gender'}))

    class Meta:
        model = Student
        fields = ['first_name','last_name','email','student_number']
