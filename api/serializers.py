from rest_framework import serializers
from .models import VaccinationData

class covidVaccinationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationData
        fields = (
            'country',
            'iso_code',
            'date',
            'total_vaccinations',
            'people_vaccinated',
            'people_fully_vaccinated',
            'daily_vaccinations_raw',
            'daily_vaccinations',
            'total_vaccinations_per_hundred',
            'people_vaccinated_per_hundred',
            'people_fully_vaccinated_per_hundred',
            'daily_vaccinations_per_million',
            'vaccines',
            'source_name',
            'source_website'
        )