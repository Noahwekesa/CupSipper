from django.urls import path
from . import views

urlpatterns = [
    path('create_notes/', views.create_notes, name="create-notes"),
]
