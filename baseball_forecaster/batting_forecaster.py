
# coding: utf-8

# In[ ]:

import math
import random
random.seed(5)

import pandas as pd
import numpy as np

from numpy.random import permutation
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsRegressor


# In[ ]:

with open("new_batting.csv", "r") as csvdata:
    batting_data = pd.read_csv(csvdata)

print (batting_data.columns.values)


# In[ ]:

selected_player = batting_data[batting_data["player_id"] == "bautijo02"].iloc[6]
# print selected_player
distance_columns = ["AB","2B","3B","HR"]

def euclidean_distance(row):
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

# jose_bautista_dist = batting_data.apply(euclidean_distance, axis=1)
# print jose_bautista_dist

batting_numeric = batting_data[distance_columns]
batting_normalized = (batting_numeric - batting_numeric.mean()) / batting_numeric.std()


# In[ ]:

batting_normalized.fillna(0, inplace=True)

# print batting_data["player_id"] == "bautijo02"

# get jose bautista
jose_bautista_normalized = batting_normalized[batting_data["player_id"] == "bautijo02"]

# reduce to single year
jose_bautista_normalized = jose_bautista_normalized.iloc[6]
# print jose_bautista_normalized

euclidean_distances = batting_normalized.apply(lambda row: distance.euclidean(row, jose_bautista_normalized), axis=1)


# In[ ]:

# single player lookup
distance_data = pd.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_data.sort("dist", inplace=True)
# 0 will should be player himself, 1 is nearest
player_lookup = [0,1,2,3,4,5]
for player_to_lookup in player_lookup:
    nearest_match = distance_data.iloc[player_to_lookup]["idx"]
#     most_similar_player = batting_data.loc[int(nearest_match)]["player_id"]
    most_similar_player = batting_data.loc[int(nearest_match)]
    print most_similar_player


# In[ ]:

random_indices = permutation(batting_data.index)
test_cutoff = math.floor(len(batting_data)/3)
test_dataset = batting_data.loc[random_indices[1:test_cutoff]]
train_dataset = batting_data.loc[random_indices[test_cutoff:]]


# In[ ]:

# run model
explanatory_vars = ["total_years", "AB", "2B"]
independent_var = ["HR"]

knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(train_dataset[explanatory_vars], train_dataset[independent_var])
predictions = knn.predict(test_dataset[explanatory_vars])

observed = test_dataset[independent_var]

mse = (((predictions - observed) ** 2).sum()) / len(predictions)

print mse ** (1/2.0)

# print predictions[:5]
# print test_dataset[:5]
test_dataset["predHR"] = predictions
print test_dataset[test_dataset["player_id"] == "cabremi01"].sort("year_id")

