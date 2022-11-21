from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from base.models import User, Teacher, Student

class CreateUserTests(TestCase):
    """Testing usercreation on the client side"""
    client = APIClient()
    path = reverse('register')

    def test_creating_student_user(self):
        """Test for creating a student user"""
        payload = {
            'username':'Ankit',
            'usertype':'s',
            'password1':'B5BJxT46gExinn7',
            'password2':'B5BJxT46gExinn7'
        }
        res = self.client.post(self.path, payload)
        self.assertEqual(res.status_code, 302)

        user = User.objects.get(username=payload['username'])
        student = Student.objects.get(user=user)

        self.assertEqual(student.user.username, payload['username'])

    def test_creating_teacher_user(self):
        """Test for creating a teacher user"""
        payload = {
            'username':'Ankit',
            'usertype':'t',
            'password1':'B5BJxT46gExinn7',
            'password2':'B5BJxT46gExinn7'
        }
        res = self.client.post(self.path, payload)
        self.assertEqual(res.status_code, 302)

        user = User.objects.get(username=payload['username'])
        teacher = Teacher.objects.get(user=user)

        self.assertEqual(teacher.user.username, payload['username'])
