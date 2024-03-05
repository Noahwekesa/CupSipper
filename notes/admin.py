from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_Display = ["title", "content"]


admin.site.register(Note, MarkdownxModelAdmin)
