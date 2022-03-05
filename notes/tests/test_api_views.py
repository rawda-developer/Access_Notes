from rest_framework.test import APITestCase
from notes.models import Note
from django.contrib.auth.models import User


class NoteCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin')
        self.user.save()
        self.client.login(
            username='admin', password='admin')

    def test_login_user(self):
        self.assertTrue(self.client.login(
            username='admin', password='admin'))

    def test_create_product(self):
        initial_note_count = Note.objects.count()
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
        self.client.logout()
        self.user.delete()


class NoteDestroyTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin')
        self.user.save()
        self.client.login(username='admin',
                          password='admin')
        self.note1 = Note.objects.create(
            title='Note1', text='Hello world', user=self.user)
        self.note1.save()

    def test_login_user(self):
        self.assertTrue(self.client.login(
            username='admin', password='admin'))

    def test_delete_note(self):
        note_id = self.note1.id
        print(note_id)
        initial_note_count = Note.objects.count()
        response = self.client.delete(f'/api/v1/notes/{note_id}/')
        self.assertEqual(response.status_code, 204)

        self.assertEqual(Note.objects.count(), initial_note_count - 1)

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.note1.delete()

class NoteListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin')
        self.user.save()
        self.client.login(username='admin',
                          password='admin')
        self.note1 = Note.objects.create(
            title='Note1', text='Hello world', user=self.user)
        self.note1.save()

    def test_list_all_notes(self):
        initial_note_count = Note.objects.count()
        response = self.client.get('/api/v1/notes/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), initial_note_count)
    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.note1.delete()
