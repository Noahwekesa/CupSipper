from django.shortcuts import render
from .models import Note


def dashboard(request):
    notes = Note.objects.order_by("-created_at")
    context = {"notes": notes}
    return render(request, "notes/dashboard.html", context)
