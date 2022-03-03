from django import forms
from .models import Note
class NoteCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    text = forms.Textarea()
    class Meta:
        model = Note
        fields = ['title', 'text']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']