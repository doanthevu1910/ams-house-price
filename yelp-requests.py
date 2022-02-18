import requests
import json

api_key = '_Dlccx0wbxIfFyliclqmeoeNxTmn2vSwTkw_AFFYc6mXxUhtHimWH2Ffq1cU17BEkIS1q03RS4XQxNiR9B1IL0q1gHw3zB2gsOkEoHKIJbYgv2cUeSNrYU5-07oOYnYx'
headers = {'Authorization': 'Bearer %s' % api_key}
url = 'https://api.yelp.com/v3/businesses/search'

rating = []
zipcode = []
prices = []

offset = 1

#7 pages of 50 businesses = 350 businesses

while offset <= 7:
    params = {'term': 'Restaurants', 'location': 'amsterdam', 'limit': 50, 'offset': offset}
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    n = 0
    while n <= 50:
        try:
            price_data = parsed["businesses"][n]['price']
            ratings_data = parsed["businesses"][n]['rating']
            zipcode_data = parsed["businesses"][n]["location"]["zip_code"]

            rating.append(ratings_data)
            zipcode.append(zipcode_data)
            prices.append(price_data)

        except:
            pass
    offset += 1
    print(offset)

