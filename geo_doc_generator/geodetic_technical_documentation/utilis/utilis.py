import os
from django.views.generic import DetailView
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_technical_documentation.serializers import GeodeticWorkDocumentsSerializer


class DeleteOldPDF:
    def _delete_file(path):
        if os.path.isfile(path):
            os.remove(path)


class TableOfContent:
    values = [
        "table_of_content",
        "technical_description",
        "network_draft",
        "geodetic_network",
        "geodetic_coordinates",
        "comparision_map",
        "field_draft",
        "list_coordinates",
        "change_list_buildings",
        "change_list_plot",
    ]


class DocumentPreview(DetailView):
    model = GeodeticWork

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        return pdf_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_geodetic_work_context(self.object)
        return context
