import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv("data1.csv")

data = df.drop(['price', 'postcode', 'year', 'latitude', 'longitude'], axis=1)

corr_matrix = data.corr()

sn.heatmap(corrMatrix, annot=True)
plt.show()