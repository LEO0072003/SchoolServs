from django.contrib import admin
from .models import Student, Teacher,User, Class, Subject
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Subject)
