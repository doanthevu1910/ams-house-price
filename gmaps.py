import gmaps
import pandas as pd

df = pd.read_csv("data.csv")

gmaps.configure(api_key='AIzaSyCzzXQDrgXt-H_IeMlvl8s26bcm9vX_uqM')

fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(
  df[['latitude','longitude']],
  weights=df['house_price'],
  max_intensity = 1000,
  point_radius=6.0
)

fig.add_layer(heatmap_layer)
fig