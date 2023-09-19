import csv
import os
import re
from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .forms import BatchFileGeoInfoForm, HeightConversionForm


class GeodeticToolsView(TemplateView):
    template_name = "geodetic_tools/main.html"


class HeightConversionView(FormView):
    form_class = HeightConversionForm
    template_name = "geodetic_tools/height_conversion.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            height_difference = form.cleaned_data.get("height_difference")
            conversion_file = form.cleaned_data.get("conversion_file")
            df_conversion_file = pd.read_csv(conversion_file, sep=" ", header=None)
            df_conversion_file[3] = df_conversion_file[3] + height_difference
            response_converted_file = HttpResponse(content_type="text/csv")
            response_converted_file[
                "Content-Disposition"
            ] = 'attachment; filename="converted_file.txt"'
            df_conversion_file.to_csv(
                response_converted_file, sep="\t", header=False, index=False
            )
            return response_converted_file
        else:
            return render(request, self.template_name, {"form": form})


class BatchFileGeoInfoView(FormView):
    form_class = BatchFileGeoInfoForm
    template_name = "geodetic_tools/batch_geo-info.html"

    def correct_conversion_file(self, conversion_file):
        file_content = conversion_file.read().decode("utf-8")
        splited_file_content = file_content.splitlines()
        new_file_content = ""
        for line in splited_file_content:
            line = re.sub(r"^\s+", "", line)  # usuwa spacje na początku każdego wiersza
            line = re.sub(
                r"\s+", " ", line
            )  # zamienia wielokrotne spację na jedną spację
            new_file_content += line
            new_file_content += "\n"
        corrected_file = BytesIO()
        corrected_file.write(bytes(new_file_content, encoding="utf-8"))
        corrected_file.seek(0)
        return corrected_file

    def check_separator_setting(self, conversion_file):
        delimiters = [" ", "\t"]
        file_content = conversion_file.read().decode("utf-8")
        delimiter_in_file = csv.Sniffer().sniff(file_content, delimiters).delimiter
        return delimiter_in_file

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            date = form.cleaned_data.get("date")
            id_work = form.cleaned_data.get("id_work")
            conversion_file = form.cleaned_data.get("conversion_file")
            delimiter_in_file = self.check_separator_setting(conversion_file)
            conversion_file.seek(0)
            if delimiter_in_file == " ":
                corrected_file = self.correct_conversion_file(conversion_file)
                data = pd.read_csv(
                    corrected_file, sep=delimiter_in_file, header=None
                )  # utworzenie dataframe z pliku z pikietami
                data[4] = "GSPPRB"
                data[5] = "O"
                data[6] = id_work
                data[7] = date
                wynik = data[
                    [4, 0, 1, 2, 3, 3, 5, 6, 7]
                ]  # tabela x, y ,h, rzg, kod, rodzja pom -pom. na osnowę, data pomiaru, kerg.n
            else:
                data = pd.read_csv(
                    conversion_file, sep=delimiter_in_file, header=None
                )  # utworzenie dataframe z pliku z pikietami
                data[4] = "GSPPRB"
                data[5] = "O"
                data[6] = id_work
                data[7] = date
                wynik = data[
                    [4, 0, 1, 2, 3, 3, 5, 6, 7]
                ]  # tabela x, y ,h, rzg, kod, rodzja pom -pom. na osnowę, data pomiaru, kerg.n
            coordinates = wynik.to_csv(
                sep="|", index=False, header=False, float_format="%.2f"
            )  # eksport do txt/csv - z zachowaniem 2 miejsc po przecinku
            last_line_in_file = "#Koniec"
            begining_file1 = (
                "# Plik wsadowy GEO-INFO 7, wygenerowany przez GeoDocGenerator"
            )
            begining_file2 = "#_SEPARATOR=|"
            begining_file3 = "#Punkty inne=_code.n|_number|_X|_Y|_H|RZG|MPD.n|KRG.n|DTP"
            str_after_conversion = (
                begining_file1
                + "\n"
                + begining_file2
                + "\n"
                + begining_file3
                + "\n"
                + coordinates
                + last_line_in_file
                + "\n"
            )

            file_after_conversion = HttpResponse(content_type="text/csv")
            file_after_conversion[
                "Content-Disposition"
            ] = 'attachment; filename="file_after_conversion.wsd"'
            file_after_conversion.write(str_after_conversion)
            return file_after_conversion
        else:
            return render(request, self.template_name, {"form": form})
