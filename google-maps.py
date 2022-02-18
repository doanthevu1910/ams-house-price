from googleplaces import GooglePlaces, types, lang
import numpy as np

google_places = GooglePlaces(api_key="AIzaSyAoqfPlFnCtV5IeXSL_4s7ry0V1HQPGgD8")

point1 = (52.3791, 4.9003) #centraal

query_result = google_places.nearby_search(
        lat_lng={'lat': point1[0], 'lng': point1[1]},
        radius=1000,
        types=[types.TYPE_FOOD])

len(query_result.places)

place = query_result.places[1]

place.get_details()
reviews = place.details['reviews']

len(reviews)

reviews[0]['rating']