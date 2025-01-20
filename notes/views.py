import json
from django.shortcuts import render

from notes.models import Notes
from notes.forms import NotesForm

def notes(request):
    if request.method == 'POST':
        if 'noteId' not in request.POST:
            form = NotesForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            id_data = request.POST.get('noteId')
            Notes.objects.get(id=int(id_data)).delete()

    form = NotesForm()

    data = Notes.objects.all().order_by('-id')
    context = {'data' : data,
               'title' : 'Заметки',
               'form' : form}
    return render(request, "main/notes.html", context)