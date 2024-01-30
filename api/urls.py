from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("notes", views.getNotes),
    path("notes/<id>", views.getNote),
    path("createNote", views.createNote),
    path("updateNote", views.updateNote),
    path("deleteNote", views.deleteNote),
]
