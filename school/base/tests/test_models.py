from django.test import TestCase
from base.models import User, Teacher, Student
# Create your tests here.

class UserCreationsTests(TestCase):
    def test_for_user_creation(self):
        """Test for user Creation"""
        user = User.objects.create(
            username = 'Abcs',
            name = 'Abc',
            usertype = 's'
        )
        user_ = User.objects.get(username = user.username)
        self.assertEqual(user.name, user_.name)

