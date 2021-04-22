import csv
import os

path = "/Users/bryanyi/Desktop/SWE_Portfolio/COVID_Vaccine_tracker/backend"
os.chdir(path)

from api.models import VaccinationData

with open("vaccinations_data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        mydata = VaccinationData(
            country=row['country'],
            iso_code=row['iso_code'],
            date=row['date'],
            total_vaccinations=row['total_vaccinations'],
            people_vaccinated=row['people_vaccinated'],
            people_fully_vaccinated=row['people_fully_vaccinated'],
            daily_vaccinations_raw= row['daily_vaccinations_raw'],
            daily_vaccinations=row['daily_vaccinations'],
            total_vaccinations_per_hundred=row['total_vaccinations_per_hundred'],
            people_vaccinated_per_hundred=row['people_vaccinated_per_hundred'],
            people_fully_vaccinated_per_hundred=row['people_fully_vaccinated_per_hundred'],
            daily_vaccinations_per_million=row['daily_vaccinations_per_million'],
            vaccines=row['vaccines'],
            source_name=row['source_name'],
            source_website=row['source_website']
        )
        mydata.save()
