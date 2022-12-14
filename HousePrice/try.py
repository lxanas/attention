import numpy as np
import pickle
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import h5py
import json

# load dataset
data = pd.read_csv("data_for_analysis.csv", delimiter=',')
dataset = np.asarray(data)
# split into input (X) and output (Y) variables
X = dataset[:, 2:10]
Y = dataset[:, 1:2]
print(dataset.shape)
print(X.shape)
print(Y.shape)
print(X[:3])
print(Y[:3])
'''     Now we can define different Keras Models that will be different 
        with respect to 'number of hidden layers', 'number of epochs' and
        'nuerons in the initial layer'.
'''
# define base model

# create model (this is the main structure of what the model will be)
model = Sequential()
model.add(Dense(8, input_dim=8, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal'))
# Compile model (this tells how the model is to be trained)
model.compile(loss='mse', optimizer='adam')

seed = 7
# np.random.seed(seed)
# evaluate model with standardised dataset
# estimator = KerasRegressor(build_fn = baseline_model , epochs = 100 , batch_size = 1 , verbose = 1)

# evaluating model using the kfold method
# kfold = KFold(n_splits=10)
# results = cross_val_score(model, X, Y, cv=kfold)
# print("Results: %.4f (%.4f) MSE" % (results.mean(), results.std()))

print("FITTING THE MODEL NOW")
# fitting the model
model.fit(X, Y, batch_size=16, epochs=100)

# saving the model by serializing it using json (same thing can be done using YAML)
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)
# model.save_weights("model.h5")
#
# print("MODEL HAS BEEN SAVED SUCCESSFULLY")
