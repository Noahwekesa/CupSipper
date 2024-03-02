from django import forms

from notes.models import Note


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "content")
