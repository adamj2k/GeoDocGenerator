from io import BytesIO
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import DetailView
from geodetic_work.models.document import *
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_technical_documentation.serializers import GeodeticWorkDocumentsSerializer
from xhtml2pdf import pisa


class GeneratePdf(DetailView):
    model = GeodeticWork

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
        status = pisa.pisaDocument(BytesIO(html.encode("utf-8")), buffer)
        buffer.seek(0)
        pdf_file = buffer.read()
        if not status.err:
            return pdf_file.decode("ISO8859-2")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        pdf_contex = self.get_geodetic_work_context(self.object)
        pdf_generation = self.generate_pdf(
            "geodetic_work/document_template.html", pdf_contex
        )
        response = HttpResponse(
            pdf_generation.encode("ISO8859-2"), content_type="application/pdf"
        )
        filename = f"Operat_{self.object.id_work}.pdf"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response
