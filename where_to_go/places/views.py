from django.shortcuts import render
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
        'places_geojson':
        {
            "type": "FeatureCollection",
            "features": features
            }
        }
    return render(request, 'index.html', context=context)
