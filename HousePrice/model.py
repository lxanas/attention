import pandas as pd
import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from matplotlib import pyplot as plt


def read_data(file):
    raw_data = pd.read_csv(file)
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
    return raw_data


train = read_data("train.csv")
test = read_data("test.csv")


# raw_data.info()
# print(raw_data[:30])

# print(np.array((raw_data)))
def create_dataset(data):
    x, y = [], []
    for i in range(len(data)):
        x.append(data[i][1:])
        y.append(data[i][0])
    return np.array(x), np.array(y)


x, y = create_dataset(np.array(train))
x_test, y_test = create_dataset(np.array(test))
print(x.shape)
print(y.shape)


# print(x)

def create_model():
    model = Sequential()

    model.add(Dense(128, input_shape=(13,), activation='relu', name='dense_1'))
    model.add(Dense(64, activation='relu', name='dense_2'))
    model.add(Dense(32, activation='relu', name='dense_3'))
    model.add(Dense(1, activation='linear', name='dense_output'))

    model.compile(optimizer='adam', loss='mae', metrics=['mse'])
    return model


# print(x[:3])
# x = x.reshape(-1, 1, 13)
# y = y.reshape(-1, 1, 1)
print(x.shape)
print(y.shape)
# print(x[:3])
model = create_model()
history = model.fit(x, y, epochs=100, batch_size=128, validation_data=(x_test, y_test))
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()
