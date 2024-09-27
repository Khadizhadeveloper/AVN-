from django.contrib import admin
from .models import Student, Grade, Subject

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)