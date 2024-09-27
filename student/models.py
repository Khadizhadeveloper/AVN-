from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    OTHER = 'Other', 'Other'


class Student(models.Model):
    COURSE_CHOICES = (
        ('1 курс', '1 курс'),
        ('2 курс', '2 курс'),
        ('3 курс', '3 курс'),
        ('4 курс', '4 курс'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=18)
    email = models.EmailField()
    student_number = models.CharField(max_length=15)
    gender = models.CharField(choices=Gender.choices, max_length=15, default=Gender.OTHER)
    education = models.CharField(max_length=100)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES, default='1 курс')
    major = models.CharField(max_length=100, default='sciences')
    image = models.ImageField(upload_to='student/', null=True, blank=True)

    def calculate_gpa(self):
        grades=self.grades.all()
        if not grades:
            return None
        total=sum(grade.grade for grade in grades)
        return round(total/grades.count(),2)


    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(default=2.00,max_digits=3, decimal_places=2)

    def __str__(self):
        return f'{self.student.first_name, self.student.last_name} - {self.subject.name}: {self.grade}'