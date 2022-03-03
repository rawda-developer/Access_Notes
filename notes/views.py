from .forms import NoteCreateForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

class NoteCreateView(CreateView):
    model = Note
    template_name = 'notes/notes_create.html'
    success_url = '/'
    form_class = NoteCreateForm


class NoteDeleteView(DeleteView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_delete.html'
    success_url = '/'
    form_class = NoteCreateForm

class NoteUpdateView(UpdateView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_update.html'
    success_url = '/'
    form_class = NoteCreateForm

