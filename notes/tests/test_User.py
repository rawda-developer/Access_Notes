from django.test import TestCase, Client
from notes.models import Note
from django.contrib.auth.models import User
import time
from django.urls import reverse


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1,
                                        username='user123', email='user@gmail.com', password='password123')
        self.user.save()
        self.client = Client()
        self.client.login(username=self.user.username,
                          password=self.user.password)
        self.note1 = Note.objects.create(
            title='note1', text='My note', user=self.user)
        self.note1.save()
        self.note2 = Note.objects.create(
            title='note1', text='My note', user=self.user)
        self.note2.save()

    def authorize_user(self):
        response = self.client.post('/login/', data={
            'username': self.user.username,
            'password': self.user.password,
        })
        return response

    def test_authorize_user(self):
        response = self.authorize_user()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.user.is_authenticated)

    def test_signup_is_correct(self):
        self.client.logout()
        new_user = User.objects.create(
            username='user1', password='user1 password', email='user1@gmail.com')

        response = self.client.get(reverse('signup'), data={
            'username': new_user.username,
            'password': new_user.password})
        self.assertEqual(response.status_code, 200)
        polled_user = User.objects.get(id=new_user.id)
        self.assertEqual(polled_user.username, 'user1')

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.note1.delete()
        self.note2.delete()
