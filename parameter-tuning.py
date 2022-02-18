from sklearn.model_selection import RandomizedSearchCV

# #trees in random forest
n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
# #features to consider at every split
max_features = ['auto', 'sqrt']
# Max number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
max_depth.append(None)
# Min number of samples required to split a node
min_samples_split = [2, 5, 10]
# Min number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)

rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations
rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2, random_state=2022, n_jobs=-1)
# Fit the random search model
rf_random.fit(data_train, target_train)

print(rf_random.best_params_)