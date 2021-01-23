from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.


class HomeView(ListView):

    """ Home View Definition """

    model = models.Note
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "notes"
