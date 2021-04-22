import os
import logging
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import VaccinationData

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import covidVaccinationDataSerializer


class most_vaccinated(APIView):
    def get(self, request, *args, **kwargs):
        mySQL="""
            SELECT *
            FROM api_vaccinationdata
            WHERE total_vaccinations IN (
	        SELECT MAX(total_vaccinations)
            FROM api_vaccinationdata
            )
            """
        
        querySet = VaccinationData.objects.raw(mySQL)
    
        serializer = covidVaccinationDataSerializer(querySet, many=True)
        return Response(serializer.data)

class all_countries_vaccination_data(APIView):
    
    def get(self, request, *args, **kwargs):
        
        mySQL = """
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Algeria'
            ) && country = 'Algeria'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Andorra'
            ) && country = 'Andorra'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Argentina'
            ) && country = 'Argentina'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Austria'
            ) && country = 'Austria'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Bahrain'
            ) && country = 'Bahrain'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Argentina'
            ) && country = 'Argentina'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Bangladesh'
            ) && country = 'Bangladesh'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Belgium'
            ) && country = 'Belgium'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Bermuda'
            ) && country = 'Bermuda'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Bolivia'
            ) && country = 'Bolivia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Brazil'
            ) && country = 'Brazil'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Bulgaria'
            ) && country = 'Bulgaria'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Canada'
            ) && country = 'Canada'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Cayman Islands'
            ) && country = 'Cayman Islands'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Chile'
            ) && country = 'Chile'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'China'
            ) && country = 'China'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Costa Rica'
            ) && country = 'Costa Rica'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Croatia'
            ) && country = 'Croatia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Cyprus'
            ) && country = 'Cyprus'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Czechia'
            ) && country = 'Czechia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Denmark'
            ) && country = 'Denmark'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Ecuador'
            ) && country = 'Ecuador'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Egypt'
            ) && country = 'Egypt'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'England'
            ) && country = 'England'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Estonia'
            ) && country = 'Estonia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Faeroe Islands'
            ) && country = 'Faeroe Islands'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Finland'
            ) && country = 'Finland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'France'
            ) && country = 'France'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Germany'
            ) && country = 'Germany'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Gibraltar'
            ) && country = 'Gibraltar'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Greece'
            ) && country = 'Greece'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Greenland'
            ) && country = 'Greenland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Guernsey'
            ) && country = 'Guernsey'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Hungary'
            ) && country = 'Hungary'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Iceland'
            ) && country = 'Iceland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'India'
            ) && country = 'India'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Indonesia'
            ) && country = 'Indonesia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Ireland'
            ) && country = 'Ireland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Isle of Man'
            ) && country = 'Isle of Man'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Israel'
            ) && country = 'Israel'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Italy'
            ) && country = 'Italy'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Jersey'
            ) && country = 'Jersey'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Kuwait'
            ) && country = 'Kuwait'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Lativa'
            ) && country = 'Lativa'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Liechtenstein'
            ) && country = 'Liechtenstein'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Lithuania'
            ) && country = 'Lithuania'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Luxembourg'
            ) && country = 'Luxembourg'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Maldives'
            ) && country = 'Maldives'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Malta'
            ) && country = 'Malta'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Mexico'
            ) && country = 'Mexico'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Monaco'
            ) && country = 'Monaco'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Morocco'
            ) && country = 'Morocco'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Myanmar'
            ) && country = 'Myanmar'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Nepal'
            ) && country = 'Nepal'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Netherlands'
            ) && country = 'Netherlands'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Northern Cyprus'
            ) && country = 'Northern Cyprus'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Northern Ireland'
            ) && country = 'Northern Ireland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Norway'
            ) && country = 'Norway'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Oman'
            ) && country = 'Oman'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Panama'
            ) && country = 'Panama'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Poland'
            ) && country = 'Poland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Portugal'
            ) && country = 'Portugal'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Romania'
            ) && country = 'Romania'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Russia'
            ) && country = 'Russia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Saint Helena'
            ) && country = 'Saint Helena'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Russia'
            ) && country = 'Russia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Saint Helena'
            ) && country = 'Saint Helena'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Saudi Arabia'
            ) && country = 'Saudi Arabia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Scotland'
            ) && country = 'Scotland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Serbia'
            ) && country = 'Serbia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Seychelles'
            ) && country = 'Seychelles'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Singapore'
            ) && country = 'Singapore'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Slovakia'
            ) && country = 'Slovakia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Slovenia'
            ) && country = 'Slovenia'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Spain'
            ) && country = 'Spain'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Sri Lanka'
            ) && country = 'Sri Lanka'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Sweden'
            ) && country = 'Sweden'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Switzerland'
            ) && country = 'Switzerland'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Turkey'
            ) && country = 'Turkey'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'United Arab Emirates'
            ) && country = 'United Arab Emirates'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'United Kingdom'
            ) && country = 'United Kingdom'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'United States'
            ) && country = 'United States'
            UNION
            SELECT *
            FROM api_vaccinationdata
            WHERE date = (
                SELECT MAX(date) FROM api_vaccinationdata WHERE country = 'Wales'
            ) && country = 'Wales'

            """
        
        querySet = VaccinationData.objects.raw(mySQL)
    
        serializer = covidVaccinationDataSerializer(querySet, many=True)
        return Response(serializer.data)
        
