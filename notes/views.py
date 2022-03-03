from django.views.generic import ListView
from .models import Note
class NoteListView(ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
