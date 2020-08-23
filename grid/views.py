from django.shortcuts import render
from django.views.generic import ListView
from .models import Grid, GridElement


def root(request):
    context = {}
    return render(request, "index.html", context)


class GridView(ListView):
    model = Grid


class GridElementView(ListView):
    model = GridElement
