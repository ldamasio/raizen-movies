from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .serializers import FilmSerializer
import requests

class FilmListView(APIView):
    def get(self, request, format=None):
        try:
            url = 'https://the-one-api.dev/v1/films'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            print (data)

            for film_data in data['results']:
                film, created = Film.objects.get_or_create(
                    title=film_data['title'],
                    defaults={
                        'release_date': film_data['release_date'],
                        'director': film_data['director'],
                        'opening_crawl': film_data['opening_crawl'],
                        'producers': ', '.join(film_data['producers']),
                    }
                )

            films = Film.objects.all()
            serializer = FilmSerializer(films, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)  


        except requests.exceptions.RequestException as e:
            return Response({'error': f'Error fetching data from The One API: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': f'Unexpected error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
