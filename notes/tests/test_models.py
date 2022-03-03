from django.test import TestCase
from notes.models import Note
from django.contrib.auth.models import User


class NoteModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1,
                                        username='user123', email='user@gmail.com', password='password123')
        self.user.save()
        self.note1 = Note.objects.create(
            title='note1', text='My note', user=self.user)
        self.note1.save()
        self.note2 = Note.objects.create(
            title='note1', text='My note', user=self.user)
        self.note2.save()

    def test_notes_count_is_correct(self):
        count = Note.objects.count()
        self.assertEqual(count, 2)

    def test_create_new_note(self):
        initial_count = Note.objects.count()
        new_note = Note.objects.create(
            title='New Note', text='My awesome note', user=self.user)
        new_note.save()
        self.assertEqual(Note.objects.count(), initial_count + 1)
        old_note = Note.objects.get(id=new_note.id)
        self.assertEqual(old_note.title, 'New Note')

    def test_update_new_note(self):
        initial_count = Note.objects.count()
        note = Note.objects.all()[0]
        old_title = note.title
        note.title = 'My Note!'
        note.save()
        self.assertNotEqual(Note.objects.all()[0].title, old_title)
        self.assertEqual(Note.objects.count(), initial_count)

    def test_delete_new_note(self):
        initial_count = Note.objects.count()
        note = Note.objects.all()[0]
        note_id = note.id
        note.delete()
        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=note_id)
        self.assertEqual(Note.objects.count(), initial_count - 1)

    def tearDown(self):
        self.user.delete()
        self.note1.delete()
        self.note2.delete()
