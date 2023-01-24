from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from .forms import HeightConversionForm
import pandas as pd


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
