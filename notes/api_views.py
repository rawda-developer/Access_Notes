from rest_framework import generics
from .serializers import NoteSerializer
from .models import Note


class NoteCreateAPI(generics.CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class NoteRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    lookup_field = 'id'
    serializer_class = NoteSerializer

    def delete(self, request, *args, **kwargs):
        note_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('note_data_{}'.format(note_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            note = response.data
            cache.set('note_data_{}'.format(note['id']), {
                'title': note['title'],
                'text': note['text'],
                'user': note['user'],
            })
        return response


class NoteListAPI(generics.ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
