from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Grid


def root(request):
    if not request.user.is_authenticated:
        context = {}
        return render(request, "index.html", context)
    else:
        return redirect(reverse("grids"))


class GridListView(LoginRequiredMixin, ListView):
    model = Grid


class GridDetailView(LoginRequiredMixin, DetailView):
    model = Grid
