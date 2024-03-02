from django_tables2 import tables
from .models import Note


class NoteTable(tables.Table):
    class Meta:
        model = Note
        fields = (
            "title",
            "content",
            "created_at",
        )
        attrs = {"class": "table table-striped"}
