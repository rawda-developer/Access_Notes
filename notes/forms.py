from django import forms
from .models import Note
class NoteCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=200 , widget=forms.TextInput(attrs={'class': "form-control"}))
    text = forms.CharField(label='Text',
                           widget=forms.Textarea(attrs={'class': "form-control"}))
    class Meta:
        model = Note
        fields = ['title', 'text']

