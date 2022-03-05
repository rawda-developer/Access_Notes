from rest_framework.test import APITestCase
from notes.models import Note
from django.contrib.auth.models import User


class NoteCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user123', password='password123')
        self.user.save()
        self.client.login(
            username='user123', password='password123')

    def test_login_user(self):
        self.assertTrue(self.client.login(
            username='user123', password='password123'))

    def test_create_product(self):
        initial_note_count = Note.objects.count()
        user = {'username': 'user123', 'password': 'password123'}
        note_attrs = {
            'title': 'New Note',
            'text': 'Hello, world',
            'user': self.user.id,
        }
        response = self.client.post(
            '/api/v1/notes/new/', note_attrs)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(Note.objects.count(), initial_note_count + 1)
        for attr, expected_value in note_attrs.items():
            self.assertEqual(response.data[attr], expected_value)

    def tearDown(self):
        self.user.delete()


class NoteDestroyTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user123', password='password123')
        self.user.save()
        self.client.login(username=self.user.username,
                          password=self.user.password)
        self.note1 = Note.objects.create(
            title='Note1', text='Hello world', user=self.user)
        self.note1.save()

    def test_delete_note(self):
        note_id = self.note1.id
        print(note_id)
        initial_note_count = Note.objects.count()
        self.client.delete(f'/api/v1/notes/{note_id}/')
        self.assertEqual(Note.objects.count(), initial_note_count - 1)

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.note1.delete()
