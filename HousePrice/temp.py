import pandas as pd
import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,LSTM
from matplotlib import pyplot as plt

raw_data = pd.read_csv("data_for_analysis.csv")
raw_data.drop('block group ID', axis=1, inplace=True)
# raw_data.info()
# print(raw_data[:5])
numeric_features = raw_data.dtypes[raw_data.dtypes != 'object'].index
# print(numeric_features)

numeric_features = numeric_features[1:]
# print(numeric_features)
raw_data[numeric_features] = raw_data[numeric_features].apply(lambda x: (x - x.mean()) / (x.std()))  # z-score
# raw_data.info()
# print(raw_data[:5])
# print(type(numeric_features))
ocean = list(set(raw_data['ocean_proximity']))
# print(ocean)
raw_data = pd.get_dummies(raw_data)


# raw_data.info()
# print(raw_data[:30])

# print(np.array((raw_data)))
def create_dataset(data):
    x, y = [], []
    for i in range(len(data)):
        x.append(data[i][1:])
        y.append(data[i][0])
    return np.array(x), np.array(y)


x, y = create_dataset(np.array((raw_data)))
print(x.shape)
print(y.shape)


# print(x)


model = Sequential()
model.add(Dense(13, input_dim=13, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
model.compile(optimizer='adam', loss='mse', metrics=['mse'])



# print(x[:3])
print(x.shape)
print(y.shape)
# print(x[:3])
history = model.fit(x, y, epochs=10, batch_size=128, validation_split=0.2)
# plt.plot(history.history['loss'], label='train')
# plt.plot(history.history['val_loss'], label='test')
# plt.legend()
# plt.show()
