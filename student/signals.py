from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Subject, Grade

@receiver(post_save, sender=Student)
def create_grades_for_new_student(sender, instance, created, **kwargs):
    if created:
        subjects = Subject.objects.all()
        print(f'Creating grades for new student: {instance}')# Получить все предметы
        for subject in subjects:
            grade=Grade.objects.create(student=instance, subject=subject, grade=0)
            print(f'Created grade: {grade} for subject: {subject.name}')
