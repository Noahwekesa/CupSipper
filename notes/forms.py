from django import forms
from notes.models import Note
from martor.fields import MartorFormField


class CreateNoteForm(forms.ModelForm):
    content = MartorFormField()

    class Meta:
        model = Note
        fields = ("title", "content")
