from turtle import title
from .models import Note
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class NoteForm(forms.ModelForm):
    

    class Meta:
        model = Note
        fields = ('title', 'text')
        labels = {
            "title": "Заголовок",
            "text": "Заметка",
        }
