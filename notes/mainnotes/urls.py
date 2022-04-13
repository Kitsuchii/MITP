
from django.urls import path

from . import views
from .views import NoteDeleteView, note_edit

urlpatterns = [
    path('', views.index, name='notes'),
    path('note', views.note),
    path('note/<int:pk>/edit', views.note_edit, name='note-update'),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name='note-delete'),
]