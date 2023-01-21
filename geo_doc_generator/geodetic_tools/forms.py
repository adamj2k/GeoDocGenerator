from django import forms


class HeightConversionForm(forms.Form):
    height_difference = forms.FloatField(required=True, label="Różnica wysokości")
    conversion_file = forms.FileField(
        required=True, label="Plik do konwersji", allow_empty_file=False
    )
