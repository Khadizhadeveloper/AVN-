from django.db import models

# Create your models here.

class Gender(models.TextChoices):
    MALE = 'Male', 'male'
    FEMALE = 'Female', 'female'
    OTHER = 'Other', 'other'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age=models.PositiveSmallIntegerField(default=18)
    email = models.EmailField()
    student_number = models.CharField(max_length=15)
    gender=models.CharField(choices=Gender.choices, max_length=15, default=Gender.OTHER)
    education=models.CharField(max_length=100)
    image=models.ImageField(upload_to='student/', blank=True, null=True)

    class Meta:
        verbose_name="Студент"
        verbose_name_plural='Студенты'

    def __str__(self):
        return self.first_name, self.last_name



