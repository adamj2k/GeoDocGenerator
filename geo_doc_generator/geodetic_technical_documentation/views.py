from io import BytesIO
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.core.files import File
from geodetic_work.models.document import *
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_technical_documentation.serializers import GeodeticWorkDocumentsSerializer
from xhtml2pdf import pisa
from PyPDF2 import PdfReader, PdfMerger
from django.conf import settings


class TechnicalDescriptionGeneratePdf(DetailView):
    model = GeodeticWork

    def save_pdf_to_file(self, pdf_file):
        technical_description = TechnicalDescription.objects.get(id_work=self.object.id)
        filename = f"{self.object.id_work}_tech_desc.pdf"
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


class TechnicalDescriptionPdfPreview(DetailView):
    model = GeodeticWork
    template_name = "geodetic_work/technical_description.html"

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        return pdf_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_geodetic_work_context(self.object)
        return context


class GeodeticNetworkSurveysGeneratePDF(DetailView):
    model = GeodeticWork

    def save_pdf_to_file(self, pdf_file):
        geodetic_network_survey = GeodeticNetworkSurveyData.objects.get(
            id_work=self.object.id
        )
        self.object = self.get_object()
        filename = f"{self.object.id_work}_geo_net_survey.pdf"
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


class GeodeticNetworkSurveyPdfPreview(DetailView):
    model = GeodeticWork
    template_name = "geodetic_work/geo_network_survey.html"

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        return pdf_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_geodetic_work_context(self.object)
        return context


class GeodeticNetworkCoordinatesGeneratePDF(DetailView):
    model = GeodeticWork

    def save_pdf_to_file(self, pdf_file):
        geodetic_network_coordinates = GeodeticNetworkCoordinates.objects.get(
            id_work=self.object.id
        )
        self.object = self.get_object()
        filename = f"{self.object.id_work}_geo_net_coord.pdf"
        with open(filename, "wb+") as file:
            file.write(pdf_file)
            geodetic_network_coordinates.pdf_file = File(file, filename)
            geodetic_network_coordinates.save()
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
            "geodetic_work/geo_network_coordinates.html", pdf_contex
        )
        response = HttpResponse(pdf_generation, content_type="application/pdf")
        filename = f"Wykaz_Osn_{self.object.id_work}.pdf"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response


class GeodeticNetworkCoordinatesPdfPreview(DetailView):
    model = GeodeticWork
    template_name = "geodetic_work/geo_network_coordinates.html"

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        return pdf_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_geodetic_work_context(self.object)
        return context


class ListOfCoordinatesGeneratePDF(DetailView):
    model = GeodeticWork

    def save_pdf_to_file(self, pdf_file):
        self.object = self.get_object()
        list_of_coordinates = ListOfCoordinates.objects.get(id_work=self.object.id)
        filename = f"{self.object.id_work}_list_coord.pdf"
        with open(filename, "wb+") as file:
            file.write(pdf_file)
            list_of_coordinates.pdf_file = File(file, filename)
            list_of_coordinates.save()
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
            "geodetic_work/list_coordinates.html", pdf_contex
        )
        response = HttpResponse(pdf_generation, content_type="application/pdf")
        filename = f"Wykaz_wsp_{self.object.id_work}.pdf"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response


class ListOfCoordinatesGeneratePdfPreview(DetailView):
    model = GeodeticWork
    template_name = "geodetic_work/list_coordinates.html"

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        return pdf_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_geodetic_work_context(self.object)
        return context


class TableOfContentGenerate(DetailView):
    model = GeodeticWork

    def save_pdf_to_file(self, pdf_file):
        self.object = self.get_object()
        table_of_content = TableOfContent(id_work=self.object)
        filename = f"{self.object.id_work}_toc.pdf"
        with open(filename, "wb+") as file:
            file.write(pdf_file)
            table_of_content.pdf_file = File(file, filename)
            table_of_content.save()
        return pdf_file

    def generate_table_of_content(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        number_of_element_content = {"element_numbers": []}
        table_of_content = {
            key: pdf_context[key]
            for key in [
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
            if pdf_context[key] != None
        }
        names_table_of_content = {
            "technical_description": "Sprawozdanie techniczne",
            "network_draft": "Szkic osnowy pomiarowej",
            "geodetic_network": "Dane obserwacyjne osnowy pomiarowej",
            "geodetic_coordinates": "Wykaz współrzędnych osnowy pomiarowej",
            "comparision_map": "Mapa porównania z terenem",
            "field_draft": "Szkice polowe",
            "list_coordinates": "Wykaz współrzędnych punktów pomierzonych",
            "change_list_buildings": "Wykaz zmian danych ewidencyjnych budynków",
            "change_list_plot": "Wykaz zmian danych ewidencyjnych działek",
        }
        count = 1
        end_page = 1
        generated_table_of_content = {}
        element_numbers = []
        for element in table_of_content:
            if element in names_table_of_content:
                count += 1
                element_numbers.append(count)
                number_of_element_content.update({"element_numbers": element_numbers})
                reader_pdf_file = PdfReader(table_of_content[element].pdf_file)
                start_page = end_page + 1
                number_of_pages_in_pdf = len(reader_pdf_file.pages)
                end_page = start_page + number_of_pages_in_pdf - 1
                pages_table_of_content = f"{start_page} - {end_page}"
                generated_table_of_content.update(
                    {names_table_of_content[element]: pages_table_of_content}
                )
        return generated_table_of_content

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        table_of_content = self.generate_table_of_content(self.object)
        pdf_context.update({"table_of_content": table_of_content})
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
            "geodetic_work/table_of_content.html", pdf_contex
        )
        response = HttpResponse(pdf_generation, content_type="application/pdf")
        filename = f"Spis_{self.object.id_work}.pdf"
        content = f"inline; filename={filename}"
        response["Content-Disposition"] = content
        return response


class TableOfContentPreView(DetailView):
    model = GeodeticWork
    template_name = "geodetic_work/table_of_content.html"

    def generate_table_of_content(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        number_of_element_content = {"element_numbers": []}
        table_of_content = {
            key: pdf_context[key]
            for key in [
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
            if pdf_context[key] != None
        }
        names_table_of_content = {
            "technical_description": "Sprawozdanie techniczne",
            "network_draft": "Szkic osnowy pomiarowej",
            "geodetic_network": "Dane obserwacyjne osnowy pomiarowej",
            "geodetic_coordinates": "Wykaz współrzędnych osnowy pomiarowej",
            "comparision_map": "Mapa porównania z terenem",
            "field_draft": "Szkice polowe",
            "list_coordinates": "Wykaz współrzędnych punktów pomierzonych",
            "change_list_buildings": "Wykaz zmian danych ewidencyjnych budynków",
            "change_list_plot": "Wykaz zmian danych ewidencyjnych działek",
        }
        count = 1
        end_page = 1
        generated_table_of_content = {}
        element_numbers = []
        for element in table_of_content:
            if element in names_table_of_content:
                count += 1
                element_numbers.append(count)
                number_of_element_content.update({"element_numbers": element_numbers})
                reader_pdf_file = PdfReader(table_of_content[element].pdf_file)
                start_page = end_page + 1
                number_of_pages_in_pdf = len(reader_pdf_file.pages)
                end_page = start_page + number_of_pages_in_pdf - 1
                pages_table_of_content = f"{start_page} - {end_page}"
                generated_table_of_content.update(
                    {names_table_of_content[element]: pages_table_of_content}
                )
        return generated_table_of_content

    def get_geodetic_work_context(self, instance):
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()

        table_of_content = self.generate_table_of_content(self.object)
        pdf_context.update({"table_of_content": table_of_content})
        return pdf_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.get_geodetic_work_context(self.object)
        return context


class GeodeticWorkDocumentsPDFGenerate(DetailView):
    model = GeodeticWork

    def merge_all_pdf_documents(self, instance):
        self.object = self.get_object()
        pdf_context = dict()
        geodetic_work_serializer = GeodeticWorkDocumentsSerializer(instance)
        pdf_context = geodetic_work_serializer.serialize()
        table_of_content = {
            key: pdf_context[key]
            for key in [
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
            if pdf_context[key] != None
        }
        merger_pdf = PdfMerger()
        filename = f"Operat_{self.object.id_work}.pdf"
        print(table_of_content)
        for element in table_of_content:
            reader_pdf_file = PdfReader(table_of_content[element].pdf_file)
            merger_pdf.append(reader_pdf_file)

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
