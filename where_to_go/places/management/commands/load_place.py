from django.core.management.base import BaseCommand
import requests
from PIL import Image as PIL_Image
from io import BytesIO
from pathlib import Path
import sys
from urllib.parse import urlparse
from django.db. utils import IntegrityError
from places.models import Place, Image


sys.path.append(Path(__file__).resolve().parent.parent)


class Command(BaseCommand):
    help = 'Allows you to add new locations via json'

    def add_arguments(self, parser):
        parser.add_argument('json_addresses', nargs='*', type=str)

    def handle(self, *args, **options):
        json_addresses = options['json_addresses']
        for json_address in json_addresses:
            response = requests.get(json_address)
            response.raise_for_status()
            location = response.json()

            try:
                place, _ = Place.objects.get_or_create(
                    title=location['title'],
                    defaults={
                        'description_short': location['description_short'],
                        'description_long': location['description_long'],
                        'lng': location['coordinates']['lng'],
                        'lat': location['coordinates']['lat'],
                        }
                    )
            except IntegrityError:
                print('Это место уже добавлено. Пожалуйста, выберите другое')
                continue

            images = location['imgs']

            for image in images:
                response = requests.get(image)
                response.raise_for_status()
                image_name = urlparse(image).path.split('/')[-1]
                image = PIL_Image.open(BytesIO(response.content))
                image.save(f'media/{image_name}', save=True)
                Image.objects.get_or_create(place=place, img=image_name)
