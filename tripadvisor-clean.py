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

data = pd.read_csv('tripadvisor_data.csv')

data = data[['Name', 'City', 'Rating', 'Price Range']]

data = data[data['City'].str.contains('Amsterdam')]

data.head()