import pandas as pd
import itertools
from bs4 import BeautifulSoup
import requests
from requests import get
import time
from random import seed
from random import random
from random import randint

url = 'https://www.pararius.nl/koopwoningen/amsterdam?ac='

houses = []

headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'})

count = 1
# while loop that runs 29 times (29 pages)
while count <= 29:
    # initialize new_count at 0
    new_url = url + str(count)
    # request the response
    response = get(new_url, headers=headers)
    # parse through the html
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # in the html of the page, find all the bins with <li> and class:
    house_data = html_soup.find_all('li', class_="search-list__item search-list__item--listing")
    # print where the program is on the screen
    print(new_url)

    # if the response was not empty
    if house_data != []:
    # add to the list houses
        houses.extend(house_data)
        # random wait times
        value = random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)

    else:
        print('empty')
        break

    count += 1

len(houses)