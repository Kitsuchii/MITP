from audioop import reverse
from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from .models import Note
from .forms import NoteForm
from django.views.generic.edit import UpdateView, DeleteView
from django.http import Http404


def index(request):
    notes = Note.objects.all()
    return render(request, 'mainnotes/index.html', {'title': 'Главная страница', 'notes': notes})


def note(request):
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Ошибка'
    else:
        form = NoteForm()
    context = {'form': form, 'error': error}
    return render(request, 'mainnotes/note.html', context)


def note_edit(request, pk):
    task = Note.objects.get(id=pk)

    form = NoteForm(instance=task)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'mainnotes/note_form.html', context)


class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/"