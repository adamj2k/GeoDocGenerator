from io import BytesIO
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import DetailView
from django.core.files import File
from geodetic_work.models.document import *
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_technical_documentation.serializers import GeodeticWorkDocumentsSerializer
from geodetic_technical_documentation.utilis.utilis import DocumentPreview, DeleteOldPDF
from xhtml2pdf import pisa
from PyPDF2 import PdfReader, PdfMerger
from django.conf import settings


class GeodeticNetworkSurveysGeneratePDF(DetailView):
    model = GeodeticWork

    def save_pdf_to_file(self, pdf_file):
        geodetic_network_survey = GeodeticNetworkSurveyData.objects.get(
            id_work=self.object.id
        )
        self.object = self.get_object()
        filename = f"{self.object.id_work}_geo_net_survey.pdf"
        try:
            DeleteOldPDF._delete_file(geodetic_network_survey.pdf_file.path)
        except ValueError:
            pass
        with open(filename, "wb+") as file:
            file.write(pdf_file)
            geodetic_network_survey.pdf_file = File(file, filename)
            geodetic_network_survey.save()
        return pdf_file

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        return pdf_context

    def generate_pdf(self, template_src, context_dict=None):
        if context_dict is None:
            context_dict = {}
        template = get_template(template_src)
        html = template.render(context_dict)
        buffer = BytesIO()
        status = pisa.CreatePDF(BytesIO(html.encode("utf-8")), buffer, encoding="utf-8")
        buffer.seek(0)
        pdf_file = buffer.read()
        if not status.err:
            return self.save_pdf_to_file(pdf_file)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        pdf_contex = self.get_geodetic_work_context(self.object)
        pdf_generation = self.generate_pdf(
            "geodetic_work/geo_network_survey.html", pdf_contex
        )
        response = HttpResponse(pdf_generation, content_type="application/pdf")
        filename = f"Dane_obs_{self.object.id_work}.pdf"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response


class GeodeticNetworkSurveyPdfPreview(DocumentPreview):
    template_name = "geodetic_work/geo_network_survey.html"
