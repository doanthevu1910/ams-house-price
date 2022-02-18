import pandas as pd
import geopy
import geopy.geocoders
import time
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import datetime
now = datetime.datetime.now()
from geopy.distance import geodesic

pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("data.csv")

df['latitude'] = 0
df['longitude'] = 0
df['distance1'] = 0
df['distance2'] = 0

geocoder = Nominatim(user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
geocode = RateLimiter(geocoder.geocode, min_delay_seconds = 1, return_value_on_exception = None)
# add 1 second between calls

point1 = (52.3791, 4.9003) #centraal
point2 = (52.3382, 4.8732) #zuid

i = 0

while i <= int(len(df)) - 1:

    print(i)

    location = geocode(df['postcode'][i])

    df['latitude'][i] = location.latitude
    df['longitude'][i] = location.longitude

    distance1 = geodesic((location.latitude, location.longitude), point1).km
    distance2 = geodesic((location.latitude, location.longitude), point2).km

    df['distance1'][i] = distance1
    df['distance2'][i] = distance2

    i += 1

df['age'] = now.year - df['year']

df.to_csv("data1.csv", index=False)