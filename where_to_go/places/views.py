from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Place


def show_start_page(request):
    places = Place.objects.all()
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
                },
            "properties": {
                "title": place.point_title,
                "placeId": place.place_id,
                "detailsUrl": f"static/places/{place.place_id}.json"
                }
            } for place in places]
    print(features)

    context = {
        "type": "FeatureCollection",
        "features": features
        }

    return render(request, 'index.html', {'places_geojson': context})


def show_place_json(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    response = {
        "title": place.title,
        "imgs": [photo.img.url for photo in place.photos.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
            }
        }

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False, 'indent': 4})
