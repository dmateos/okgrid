from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Grid


def root(request):
    if not request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return redirect(reverse("grids"))


class GridListView(LoginRequiredMixin, ListView):
    model = Grid

    def get_queryset(self):
        # Limit the scope to the current user
        query = super().get_queryset()
        return query.filter(user=self.request.user)


class GridDetailView(LoginRequiredMixin, DetailView):
    model = Grid

    def get_queryset(self):
        # Limit the scope to the current user
        query = super().get_queryset()
        return query.filter(user=self.request.user)
