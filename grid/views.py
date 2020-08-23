from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import Grid


def root(request):
    if not request.user.is_authenticated:
        context = {}
        return render(request, "index.html", context)
    else:
        return redirect(reverse("grids"))


class GridListView(ListView):
    model = Grid


class GridDetailView(DetailView):
    model = Grid
