from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from geodetic_work.models.geodetic_work import GeodeticWork


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

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search", None)
        if search_query:
            queryset = queryset.filter(
                id_work__icontains=search_query
            ) | queryset.filter(work_object__icontains=search_query)
        return queryset

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor


class GeodeticWorkCreatView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = GeodeticWork
    template_name = "geodetic_work/geodetic_work_create.html"
    success_url = "geodetic-work-home"
    fields = "__all__"

    def form_valid(self, form):
        work_id = form.data.get("id_work")
        form.save()
        messages.success(self.request, f"Dodałeś nową pracę o id: {work_id} ")
        return redirect(self.success_url)

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor


class GeodeticWorkDetailsView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = GeodeticWork
    template_name = "geodetic_work/geodetic_work_details.html"
    context_object_name = "work"

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor


class GeodeticWorkEditView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = GeodeticWork
    template_name = "geodetic_work/geodetic_work_edit.html"
    context_object_name = "work"
    success_url = "geodetic-work-home"
    fields = "__all__"

    def form_valid(self, form):
        work_id = form.data.get("id_work")
        form.save()
        messages.success(self.request, f"Zaaktualizowałeś dane pracy o id: {work_id} ")
        return redirect(self.success_url)

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor
