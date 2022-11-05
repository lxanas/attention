from keras.utils.np_utils import to_categorical
import pandas as pd
import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from matplotlib import pyplot as plt

raw_data = pd.read_csv("new.csv")
raw_data.drop('ID', axis=1, inplace=True)
# raw_data.info()
# print(raw_data[:5])
numeric_features = raw_data.dtypes[raw_data.dtypes != 'object'].index
# print(numeric_features)

numeric_features = numeric_features[:19]
# print(numeric_features)
raw_data[numeric_features] = raw_data[numeric_features].apply(lambda x: (x - x.mean()) / (x.std()))  # z-score
print(raw_data[:5])
print(raw_data.shape)


# raw_data.info()
# print(raw_data[:5])
# print(type(numeric_features))
# ocean = list(set(raw_data['ocean_proximity']))
# print(ocean)
# raw_data = pd.get_dummies(raw_data)


# raw_data.info()
# print(raw_data[:30])

# print(np.array((raw_data)))
def create_dataset(data):
    x, y = [], []
    for i in range(len(data)):
        x.append(data[i][:19])
        y.append(data[i][19])
    return np.array(x), np.array(y)


x, y = create_dataset(np.array((raw_data)))

print(x.shape)
print(y.shape)

print(y[:10])
s = set()
for i in y:
    s.add(i)
print(len(s))
lst = list(s)
print(lst)
print(lst.index(1))
y_one = []
for i in range(740):
    temp_index = lst.index(y[i])
    temp = np.zeros(19)
    temp[temp_index] = 1
    y_one.append(temp)
y_one = np.array(y_one)
print(y_one[:10])
