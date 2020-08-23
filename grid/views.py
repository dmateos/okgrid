from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Grid, GridElement


def root(request):
    if not request.user.is_authenticated:
        context = {}
        return render(request, "index.html", context)
    else:
        return redirect("/grids")


class GridView(ListView):
    model = Grid


class GridElementView(ListView):
    model = GridElement
