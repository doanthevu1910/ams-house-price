import gmaps
import pandas as pd
from ipywidgets.embed import embed_minimal_html

df = pd.read_csv('data/data2.csv')

df

gmaps.configure(api_key='AIzaSyAoqfPlFnCtV5IeXSL_4s7ry0V1HQPGgD8')

fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(
  df[['latitude', 'longitude']],
  weights=df['price'],
  max_intensity=1000000,
  point_radius=6.0
)

fig.add_layer(heatmap_layer)
fig

embed_minimal_html('graphs/export.html', views=[fig])