# ams-real-estate
Predict house prices in Amsterdam based on data scraped from Pararius (compliant to ToS) and Google Places API.
#Data
request.py: Scrape Amsterdam house listings from Pararius
clean.py: Clean data to get price, postcode, size, number of bedrooms, and year constructed/last renovated
distance.py: Convert the postcode into coordinates, then calculate the distance from each houses to the Centraal Station (distance1) and Zuid Station (distance2)
gmaps.py: Draw a heatmap based on price
google-maps-rating.py: For each house, get 20 nearest restaurants/bars, and 5 most recent ratings, then calculate the average rating (nearby rating)

#EDA
