from django.urls import path
from . import views
urlpatterns = [
    path('', views.NoteListView.as_view(), name='notes.list'),
    path('notes/new/', views.NoteCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='notes.delete'),
    path('notes/<int:pk>/update/', views.NoteUpdateView.as_view(), name='notes.update'),
]
