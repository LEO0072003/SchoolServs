from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.crypto import get_random_string
# Create your models here.


class Class(models.Model):
    standard = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(12)])

    def __str__(self):
        return str(self.standard)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    class_standard = models.ManyToManyField(Class)

    def __str__(self):
        return self.name


def get_registration_number():
        u_st = get_random_string(allowed_chars='abcdefghijklmnopqrst0123456798', length=7)
        a = Student.objects.all()
        if u_st in a:
            get_registration_number()
        else:
            return u_st


class Student(models.Model):

    def get_registration_number():
        u_st = get_random_string(allowed_chars='abcdefghijklmnopqrst0123456798', length=7)
        return u_st

    name = models.CharField(max_length=50)
    class_standard = models.OneToOneField(Class, on_delete = models.DO_NOTHING)
    registration_number = models.CharField(max_length=7,default=get_registration_number(),primary_key=True)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Examination(models.Model):
    name = models.CharField(max_length=20)


class ClassSchedule(models.Model):
    class_standard = models.OneToOneField(Class, on_delete = models.DO_NOTHING)
    teacher = models.OneToOneField(Teacher,on_delete = models.DO_NOTHING)
    period = models.IntegerField()
    datetime = models.DateTimeField()



class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete = models.DO_NOTHING)
    exam = models.ForeignKey(Examination, on_delete = models.CASCADE)
    class_standard = models.ManyToManyField(Class)


