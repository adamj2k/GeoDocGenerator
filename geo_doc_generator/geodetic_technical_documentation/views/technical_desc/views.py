import os
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
from docxtpl import DocxTemplate


class TechnicalDescriptionGeneratePdf(DetailView):
    model = GeodeticWork

    def save_pdf_to_file(self, pdf_file):
        technical_description = TechnicalDescription.objects.get(id_work=self.object.id)
        filename = f"{self.object.id_work}_tech_desc.pdf"
        try:
            DeleteOldPDF._delete_file(technical_description.pdf_file.path)
        except ValueError:
            pass
        with open(filename, "wb+") as file:
            file.write(pdf_file)
            technical_description.pdf_file = File(file, filename)
            technical_description.save()
        return pdf_file

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        return pdf_context

    def generate_pdf(self, template_src, context_dict=None):
        self.object = self.get_object()
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
            "geodetic_work/technical_description.html", pdf_contex
        )
        response = HttpResponse(pdf_generation, content_type="application/pdf")
        filename = f"Sprawozdanie_{self.object.id_work}.pdf"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response


class TechnicalDescriptionPdfPreview(DocumentPreview):
    template_name = "geodetic_work/technical_description.html"


class TechnicalDescriptionGenerateDocx(DetailView):
    model = GeodeticWork

    def save_docx_to_file(self, docx_file):
        technical_description = TechnicalDescription.objects.get(id_work=self.object.id)
        filename = f"{self.object.id_work}_tech_desc.docx"
        try:
            DeleteOldPDF._delete_file(technical_description.docx_file.path)
        except ValueError:
            pass
        with open(filename, "wb+") as file:
            file.write(docx_file)
            technical_description.docx_file = File(file, filename)
            technical_description.save()
        return docx_file

    def get_geodetic_work_context(self, instance):
        docx_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        docx_context = geodetic_work_serializer.serialize()
        return docx_context

    def generate_docx(self, context_dict=None):
        self.object = self.get_object()
        if context_dict is None:
            context_dict = {}
        template_docx = os.path.join(
            settings.BASE_DIR,
            settings.STATIC_ROOT,
            "geodetic_technical_documentation\\template_inwent.docx",
        )  # TODO add path in appropriate way
        document_docx = DocxTemplate(template_docx)
        document_docx.render(context_dict)
        docx_file = document_docx.save("Sprawozdanie.docx")
        return docx_file

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        docx_contex = self.get_geodetic_work_context(self.object)
        print(docx_contex)
        docx_generation = self.generate_docx(docx_contex)
        response = HttpResponse(docx_generation, content_type="application/docx")
        filename = f"Sprawozdanie_{self.object.id_work}.docx"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response
