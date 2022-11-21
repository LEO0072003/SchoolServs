from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    usertype = models.CharField(choices=[('t','teacher'),('s','student')], max_length=1)
    name = models.CharField(max_length=50, default=None, null=True)


class Class(models.Model):
    standard = models.PositiveIntegerField(default=6, validators=[MinValueValidator(1), MaxValueValidator(12)], unique=True)


    class Meta:
        ordering = ['standard']

    def __str__(self):
        return str(self.standard)


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class_standard = models.ManyToManyField(Class)

    def __str__(self):
        return self.name



def get_registration_number():
        not_uniqe = True
        while not_uniqe:
            u_st = get_random_string(allowed_chars='abcdefghijklmnopqrst0123456798', length=7)
            if not Student.objects.filter(registration_number=u_st):
                return u_st

class Student(models.Model):
    class_standard = models.OneToOneField(Class, on_delete = models.DO_NOTHING,default=None, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=7,default=get_registration_number,primary_key=True, editable=False)

    def __str__(self):
        if self.user.name is not None:
            return self.user.name
        else:
            return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

# class Examination(models.Model):
#     name = models.CharField(max_length=20)


# class ClassSchedule(models.Model):
#     class_standard = models.ManyToManyField(Class)
#     teacher = models.ManyToManyField(Teacher)
#     period = models.IntegerField()
#     datetime = models.DateTimeField()
#     subject = models.OneToOneField(Subject, on_delete=models.DO_NOTHING)


#     class Meta:
#         unique_together = ['class_standard','period']

#     def __str__(self):
#         return str(self.class_standard)+"-"+str(self.period)


# class Marks(models.Model):
#     student = models.ForeignKey(Student,on_delete = models.CASCADE)
#     subject = models.ForeignKey(Subject,on_delete = models.DO_NOTHING)
#     exam = models.ForeignKey(Examination, on_delete = models.CASCADE)
#     class_standard = models.ManyToManyField(Class)

#     def __str__(self):
#         return self.student

