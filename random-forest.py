import pandas as pd
import numpy as np

from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data2.csv")

target = np.array(df['price'])
features = df.drop(['postcode', 'year', 'latitude', 'longitude'], axis=1)
feature_list = list(features.columns)
features = np.array(features)

kf = KFold(n_splits=10, random_state=2022, shuffle=True)

accuracies = []

for train_index, test_index in kf.split(features):
    data_train = features[train_index]
    target_train = target[train_index]

    data_test = features[test_index]
    target_test = target[test_index]

    rf = RandomForestRegressor(n_estimators=300,
                               random_state=2022,
                               criterion='mse',
                               bootstrap=True)

    rf.fit(data_train, target_train)

    predictions = rf.predict(data_test)

    errors = abs(predictions - target_test)

    print('Mean Absolute Error:', round(np.mean(errors), 2))

    mape = 100 * (errors / target_test)
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')

    accuracies.append(accuracy)

average_accuracy = np.mean(accuracies)
print('Average accuracy:', average_accuracy)

