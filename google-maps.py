from googleplaces import GooglePlaces, types, lang
import numpy as np
import pandas as pd

api_key = 'AIzaSyAoqfPlFnCtV5IeXSL_4s7ry0V1HQPGgD8'
df = pd.read_csv('data.csv')

df['nearby rating'] = 0

df.head()

lat = df['latitude'][0]
lng = df['longitude'][0]

google_places = GooglePlaces(api_key=api_key)

query_result = google_places.nearby_search(
        lat_lng={'lat': lat, 'lng': lng},
        radius=1000,
        types=[types.TYPE_FOOD])

count = 0

place_rating = []

while count <= len(query_result.places) - 1:
        place = query_result.places[count]
        try:
                place.get_details()
                reviews = place.details['reviews']

                score = []
                i = 0

                while i <= len(reviews) - 1:
                        score.append(reviews[i]['rating'])
                        i += 1

                place_rating.append(np.average(score))

        except:
                pass

        count += 1
        print(count)

np.average(place_rating)