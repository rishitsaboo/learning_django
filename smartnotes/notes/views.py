from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView,DetailView,ListView
from .forms import NotesForm
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    def get_queryset(self):
        return Notes.objects.filter(likes__gte = 1)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    

