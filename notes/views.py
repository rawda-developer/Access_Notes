from .forms import NoteCreateForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    login_url = '/admin'
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'
    login_url = '/admin'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/notes_create.html'
    success_url = '/'
    form_class = NoteCreateForm
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_delete.html'
    success_url = '/'
    login_url = '/admin'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_update.html'
    success_url = '/'
    form_class = NoteCreateForm
    login_url = '/admin'
