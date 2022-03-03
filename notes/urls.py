from django.urls import path
from . import views
urlpatterns = [
    path('', views.NoteListView.as_view(), name='notes.list'),
    path('notes/new/', views.NoteCreateView.as_view(), name='notes.new'),
]
