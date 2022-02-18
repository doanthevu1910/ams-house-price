headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'})

count = 1
# initialize new_count at 0
new_url = url + str(count)
    # request the response
response = get(new_url, headers=headers)
    # parse through the html
html_soup = BeautifulSoup(response.text, 'html.parser')
    # in the html of the page, find all the bins with <li> and class:
house_data = html_soup.find_all('li', class_="search-list__item search-list__item--listing")
    # print where the program is on the screen
print(house_data)

print(response.text)