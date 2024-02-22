from django.contrib import admin

from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content']

admin.site.register(Note, NoteAdmin)
