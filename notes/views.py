from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .tables import NoteTable
from .models import Note


@login_required
def dashboard(request):
    notes = NoteTable(Note.objects.filter(user=request.user))
    context = {"notes": notes}
    return render(request, "notes/dashboard.html", context)
