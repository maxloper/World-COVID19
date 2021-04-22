from django import forms
from api.models import covidVaccinationData

class VaccinationData(forms.ModelForm):
    class Meta:
        model = covidVaccinationData
        fields = "__all__"