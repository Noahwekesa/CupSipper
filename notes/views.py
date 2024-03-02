from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .tables import NoteTable
from .models import Note
from .forms import CreateNoteForm


@login_required
def dashboard(request):
    template_name = "notes/dashboard.html"
    notes = NoteTable(Note.objects.filter(user=request.user))
    context = {"notes": notes}
    return render(request, template_name, context)


def create_notes_view(request):
    template_name = "notes/create.html"
    form = CreateNoteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            # msg
            return redirect("dashboard")

    context = {"form": form}
    return render(request, template_name, context)


def save_data(request):
    return JsonResponse({"message": "Data saved successfully"})


# @login_required
# def create_notes_view(request):
#     if request.method == "POST":
#         form = CreateNoteForm(request.POST)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.user = request.user
#             note.save()
#             return JsonResponse({"success": True})
#         else:
#             return JsonResponse(
#                 {"success": False, "errors": form.errors},
#                 status=400,
#             )
#     else:
#         form = CreateNoteForm()
#         if request.headers.get("HTTP_HX_REQUEST", False):
#             return render(request, "notes/create.html", {"form": form})
#         else:
#             return render(request, "notes/create.html", {"form": form})
