from django.urls import path
from . import views


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create/", views.create_notes_view, name="create_notes_view"),
]

htmx_urlpatterns = [
    path("create/", views.save_data, name="save_data"),
]


urlpatterns += htmx_urlpatterns
