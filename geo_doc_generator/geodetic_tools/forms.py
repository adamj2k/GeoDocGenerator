from django import forms


class HeightConversionForm(forms.Form):
    height_difference = forms.FloatField(required=True, label="Różnica wysokości")
    conversion_file = forms.FileField(
        required=True, label="Plik do konwersji", allow_empty_file=False
    )


class BatchFileGeoInfoForm(forms.Form):
    date = forms.CharField(required=True, label="Data pomiaru", initial="RRRR-MM-DD")
    id_work = forms.CharField(
        required=True, label="Identyfikator roboty", initial="np. GK.6640.2341.2021"
    )
    conversion_file = forms.FileField(
        required=True, label="Plik ze współrzednymi", allow_empty_file=False
    )
