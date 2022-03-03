from django.shortcuts import redirect
from .forms import NoteCreateForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    login_url = '/login/'
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    
    def get_queryset(self):
        return self.request.user.notes.all()

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'
    login_url = '/login/'

    def get_queryset(self):
        return self.request.user.notes.all()

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/notes_create.html'
    success_url = '/'
    form_class = NoteCreateForm
    login_url = '/login/'

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
    login_url = '/login/'
    def get_queryset(self):
        return self.request.user.notes.all()

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_update.html'
    success_url = '/'
    form_class = NoteCreateForm
    login_url = '/login/'
    def get_queryset(self):
        return self.request.user.notes.all()
  

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'notes/signup.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('login')


class MyLoginView(LoginView):
    template_name = 'notes/login.html'
    success_url = '/'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
