import pandas as pd

n = len(houses)

price = []
postcode = []
size = []
kamers = []
year = []

i = 0

while i <= n-1:

    h = houses[i]

    pr = h.find("div", {"class": "listing-search-item__price"}).text
    pr = pr.replace(" ", "")
    pr = pr.replace("€", "")
    pr = int(pr[2:9].replace(".", ""))

    po = h.find("div", {"class": "listing-search-item__location"}).text
    po = po.replace(" ", "")
    po = po[1:7]

    s = h.find("li", {"class": "illustrated-features__item illustrated-features__item--surface-area"}).text
    s = int(s[0:(len(s)-3)])

    k = h.find("li", {"class": "illustrated-features__item illustrated-features__item--number-of-rooms"}).text
    k = int(k[0])
    # k = int(k.replace(" kamer", ""))

    y = h.find("li", {"class": "illustrated-features__item illustrated-features__item--construction-period"}).text
    y = int(y[-4:])

    price.append(pr)
    postcode.append(po)
    size.append(s)
    kamers.append(k)
    year.append(y)

    i += 1

data = {'price': price, 'postcode': postcode, 'size': size, 'kamers': kamers, 'year': year}
df = pd.DataFrame(data)
df

df.to_csv('data/data.csv', index=False)