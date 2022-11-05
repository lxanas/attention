from keras.utils.np_utils import to_categorical
import pandas as pd
import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from matplotlib import pyplot as plt

raw_data = pd.read_csv("new.csv")
raw_data.drop('ID', axis=1, inplace=True)
# raw_data.drop('Reason for absence', axis=1, inplace=True)
# raw_data.drop('Month of absence', axis=1, inplace=True)
# raw_data.drop('Transportation expense', axis=1, inplace=True)
# raw_data.drop('Service time', axis=1, inplace=True)
# raw_data.drop('Hit target', axis=1, inplace=True)
raw_data.drop('Pet', axis=1, inplace=True)
# raw_data.info()
# print(raw_data[:5])
numeric_features = raw_data.dtypes[raw_data.dtypes != 'object'].index
# print(numeric_features)

numeric_features = numeric_features[:18]
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
        x.append(data[i][:18])
        y.append(data[i][18])
    return np.array(x), np.array(y)


x, y = create_dataset(np.array((raw_data)))
s = set()
for i in y:
    s.add(i)
print(len(s))
lst = list(s)
print(lst)
print(lst.index(1))
y_one = []
for i in range(704):
    temp_index = lst.index(y[i])
    temp = np.zeros(8)
    temp[temp_index] = 1
    y_one.append(temp)
y_one = np.array(y_one)
print(y_one[:10])
print(x.shape)
print(y.shape)


# print(x)

def create_model():
    model = Sequential()

    model.add(Dense(128, input_shape=(18,), activation='sigmoid', name='dense_1'))
    model.add(Dense(64, activation='sigmoid', name='dense_2'))
    # model.add(Dense(1, activation='linear', name='dense_output'))
    model.add(Dense(8, activation='softmax', name='dense_output'))
    # model.compile(optimizer='adam', loss='mae', metrics=['mae'])
    model.compile(optimizer='adam', loss='categorical_crossentropy',
                  metrics=['accuracy'])
    # model = Sequential()
    # model.add(Dense(64, activation='relu', input_dim=19))
    # model.add(Dense(19, activation='softmax'))
    # model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
    #               metrics=['accuracy'])

    return model


# print(x[:3])
# x = x.reshape(-1, 1, 13)
# y = y.reshape(-1, 1, 1)
print(x.shape)
print(y.shape)
# print(x[:3])
model = create_model()
history = model.fit(x, y_one, epochs=40, batch_size=32, validation_split=0.3, shuffle=True)
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()
