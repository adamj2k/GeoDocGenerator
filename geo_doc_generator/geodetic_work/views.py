from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models.geodetic_work import GeodeticWork


class GeodeticWorkListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = GeodeticWork
    template_name = "geodetic_work/geodetic_work_list.html"
    context_object_name = "works"


class GeodeticWorkCreatView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    pass


class GeodeticWorkDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    pass


class GeodeticWorkUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    pass
