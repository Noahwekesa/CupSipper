from django.shortcuts import render
from .forms import CreateNotesForm


def create_notes(request):
    form = CreateNotesForm()
    content = { 'form': form}
    return render(request, 'notes/create_notes.html', content)
