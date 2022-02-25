df = pd.read_csv("data/data2.csv")

# create a new dataframe that is indexed like the trained model
newdata = pd.DataFrame().reindex_like(df)
newdata.fillna(value=0, inplace=True)

# delete the variable to be predicted
del newdata['price']
newdata = newdata.iloc[[1]]

# insert information about your apartment
newdata['kamers'] = 1
newdata['size'] = 45
newdata['nearby rating'] = 4.113475

# only change the number values in the postcode
# and string values after the _ for the rental agency
point1 = (52.3791, 4.9003) #centraal
point2 = (52.3382, 4.8732) #zuid

newdata['postcode'] = '1102AA'

location = geocode('1102AA')

newdata['latitude'] = location.latitude
newdata['longitude'] = location.longitude

newdata['distance1'] = geodesic((location.latitude, location.longitude), point1).km
newdata['distance2'] = geodesic((location.latitude, location.longitude), point2).km

newdata['age'] = 7
newdata['year'] = 2014

rf.predict(newdata)
