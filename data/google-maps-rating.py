from googleplaces import GooglePlaces, types, lang
import numpy as np
import pandas as pd

api_key = 'AIzaSyAoqfPlFnCtV5IeXSL_4s7ry0V1HQPGgD8'
df = pd.read_csv('data1.csv')

df['nearby rating'] = 0

count = 0

while count <= len(df) - 1:

        lat = df['latitude'][count]
        lng = df['longitude'][count]

        google_places = GooglePlaces(api_key=api_key)

        query_result = google_places.nearby_search(
                lat_lng={'lat': lat, 'lng': lng},
                radius=1000,
                types=[types.TYPE_FOOD])

        count1 = 0

        place_rating = []

        while count1 <= len(query_result.places) - 1:
                place = query_result.places[count1]
                try:
                        place.get_details()
                        reviews = place.details['reviews']

                        score = []
                        count2 = 0

                        while count2 <= len(reviews) - 1:
                                score.append(reviews[count2]['rating'])
                                count2 += 1

                        place_rating.append(np.average(score))

                except:
                        pass

                count1 += 1

        count += 1
        print(count)
        df['nearby rating'][count] = np.average(place_rating)

df.to_csv("data2.csv", index=False)

