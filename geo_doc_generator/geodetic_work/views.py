from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models.geodetic_work import GeodeticWork


class GeodeticWorkHome(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = GeodeticWork
    template_name = "geodetic_work/geodetic_work_home.html"
    context_object_name = "works"
    queryset = GeodeticWork.objects.all()[:5]

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor


class GeodeticWorkListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = GeodeticWork
    template_name = "geodetic_work/geodetic_work_list.html"
    context_object_name = "works"
    ordering = ["-begin_date"]
    paginate_by = 10

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor


class GeodeticWorkCreatView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    pass


class GeodeticWorkDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    pass


class GeodeticWorkUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    pass
