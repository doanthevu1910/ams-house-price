import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv("data2.csv")

data = df.drop(['price', 'postcode', 'year', 'latitude', 'longitude'], axis=1)

corr_matrix = data.corr()

sn.heatmap(corr_matrix, annot=True)
plt.show()