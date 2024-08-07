from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_work.models.document import *


class ChangeBuildingCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = ChangeListBuilding
    template_name = "geodetic_work/document_create.html"
    fields = "__all__"

    def get_initial(self):
        work_id = get_object_or_404(GeodeticWork, id=self.kwargs["pk"])
        initial = {"id_work": work_id}
        return initial

    def form_valid(self, form):
        work_id = form.data.get("id_work")
        form.save()
        messages.success(
            self.request,
            "Dodałeś dokument: Wykaz zmian danych ewidencyjnych dot. budynku",
        )
        return redirect("geodetic-work-details", work_id)

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["geodetic_work"] = get_object_or_404(GeodeticWork, id=self.kwargs["pk"])
        return context


class ChangeBuildingUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = ChangeListBuilding
    template_name = "geodetic_work/document_create.html"
    fields = "__all__"

    def form_valid(self, form):
        work_id = form.data.get("id_work")
        form.save()
        messages.success(
            self.request,
            "Zmieniłeś dane dokumentu: Wykaz zmian danych ewidencyjnych dot. budynku",
        )
        return redirect("geodetic-work-details", work_id)

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor


class ChangeBuildingDeleteView(UserPassesTestMixin, DeleteView):
    model = ChangeListBuilding
    template_name = "geodetic_work/document_delete.html"

    def test_func(self):
        geodetic_work = self.get_object()
        return self.request.user == geodetic_work.contractor
