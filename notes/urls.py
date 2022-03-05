from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .api_views import *
urlpatterns = [
    path('', views.NoteListView.as_view(), name='notes.list'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='notes.note'),
    path('notes/new/', views.NoteCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>/delete/',
         views.NoteDeleteView.as_view(), name='notes.delete'),
    path('notes/<int:pk>/update/',
         views.NoteUpdateView.as_view(), name='notes.update'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="notes/logout.html"), name='logout'),
    path('api/v1/notes/new/', NoteCreateAPI.as_view()),
    path('api/v1/notes/<int:id>/', NoteRetrieveUpdateDestroyAPI.as_view()),
]
