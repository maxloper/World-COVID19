from django.db import models

class VaccinationData(models.Model):
    country = models.CharField(max_length=100)
    iso_code = models.CharField(max_length=100, default="N/A")
    date = models.CharField(max_length=100, default="N/A")
    total_vaccinations = models.CharField(max_length=100, default="N/A")
    people_vaccinated = models.CharField(max_length=100, default="N/A")
    people_fully_vaccinated = models.CharField(max_length=100, default="N/A")
    daily_vaccinations_raw = models.CharField(max_length=100, default="N/A")
    daily_vaccinations = models.CharField(max_length=100, default="N/A")
    total_vaccinations_per_hundred = models.CharField(max_length=100, default="N/A")
    people_vaccinated_per_hundred = models.CharField(max_length=100, default="N/A")
    people_fully_vaccinated_per_hundred = models.CharField(max_length=100, default="N/A")
    daily_vaccinations_per_million = models.CharField(max_length=100, default="N/A")
    vaccines = models.CharField(max_length=100, default="N/A")
    source_name = models.CharField(max_length=100, default="N/A")
    source_website = models.CharField(max_length=1000, default="N/A")
    
    def __str__(self):
        return self.country
