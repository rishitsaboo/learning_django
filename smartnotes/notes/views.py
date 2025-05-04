from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import DetailView,ListView 

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    def get_queryset(self):
        return Notes.objects.filter(likes__gt = 1)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
