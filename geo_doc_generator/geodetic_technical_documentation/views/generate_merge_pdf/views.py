from io import BytesIO
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import DetailView
from django.core.files import File
from django.contrib import messages
from geodetic_work.models.document import *
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_technical_documentation.serializers import GeodeticWorkDocumentsSerializer
from geodetic_technical_documentation.utilis.utilis import TableOfContent, DeleteOldPDF
from xhtml2pdf import pisa
from PyPDF2 import PdfReader, PdfMerger
from django.conf import settings


class GeodeticWorkDocumentsPDFGenerate(DetailView):
    model = GeodeticWork

    def merge_all_pdf_documents(self, instance):
        self.object = self.get_object()
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        table_of_content = {
            key: pdf_context[key]
            for key in TableOfContent.values
            if pdf_context[key] != None
        }
        merger_pdf = PdfMerger()
        filename = f"Operat_{self.object.id_work}.pdf"
        for element in TableOfContent.values:
            try:
                reader_pdf_file = PdfReader(table_of_content[element].pdf_file)
            except ValueError:
                messages.error(
                    self.request,
                    f"Błąd: wygeneruj plik PDF dla {table_of_content[element]} ",
                )
                HttpResponseRedirect(
                    reverse("geodetic-work-details", kwargs={"pk": instance.id})
                )
            except KeyError:
                continue
            merger_pdf.append(reader_pdf_file)
        try:
            DeleteOldPDF._delete_file(self.object.pdf_documentation.path)
        except ValueError:
            pass
        with open(filename, "wb+") as file:
            merger_pdf.write(file)
            self.object.pdf_documentation = File(file, filename)
            self.object.save()

        merger_pdf.close()
        return self.object.pdf_documentation

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        pdf_generation = self.merge_all_pdf_documents(self.object)
        response = HttpResponse(pdf_generation, content_type="application/pdf")
        filename = f"Operat_{self.object.id_work}.pdf"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response
