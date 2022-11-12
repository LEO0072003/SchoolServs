from django.contrib import admin
from .models import Class, Subject, Student, Teacher, Examination, ClassSchedule, Marks
# Register your models here.

admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Examination)
admin.site.register(ClassSchedule)
admin.site.register(Marks)
