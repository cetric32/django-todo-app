from django.test import TestCase
from django.contrib.auth.models import User

from .models import Todo
import datetime


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='cetric',password='12345',email='cetric32@gmail.com')
        User.objects.create_user(username='kevo',password='12345',email='kevo@gmail.com')

    def test_user(self):
        cetric = User.objects.get(username='cetric')
        kevo = User.objects.get(username='kevo')

        self.assertEqual(cetric.username,'cetric')
        self.assertEqual(kevo.username,'kevo')


class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(title='market',description='go to market',owner=cetric)
        Todo.objects.create(title='wash',description='wash my clothes',owner=kevo)

    def test_todo(self):
        wash = Todo.objects.get(title='<Todo: wash>')
        market = Todo.objects.get(title='<Todo: market>')

        self.assertEqual(wash,'wash')
        self.assertEqual(market,'market')


        
