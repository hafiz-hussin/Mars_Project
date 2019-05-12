# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

# Data
data = pd.read_csv('data/CompleteDataset.csv', index_col=False)
data.head()
data.isna().sum()
data.describe()

temp_high = data.iloc[:, [3,8]]
# sort
df1 = temp_high.copy()
# df1 = temp_high.sort_index(ascending=False, axis=0)
df1['Date'] = pd.to_datetime(df1['Date'])
df1.set_index('Date', inplace=True)
df1 = df1.sort_index(ascending=True)
df1.info()

# Plot the time series
plt.style.use('fivethirtyeight')
plt.plot(df1, color='r', linewidth=3, alpha=0.8)
plt.xlabel('Date')
plt.ylabel('Pressure (hPa)')
plt.legend(prop={'size': 10})
plt.grid(color='k', alpha=0.4)
plt.show()

# outliers at two point
df1[pd.to_datetime("2017-07-01"):pd.to_datetime("2017-10-01")].plot(kind="line")
plt.show()

df1[pd.to_datetime("2018-03-01"):pd.to_datetime("2018-04-01")].plot(kind="line")
plt.show()

# try MA-7
fig, axes = plt.subplots(nrows=1, ncols=1, figsize = (12, 5))
df1.rolling(7).mean().rename(columns={"count": "Week SMA"}).plot(ax=axes, lw=0.9)
plt.show()

# try MA-24
fig, axes = plt.subplots(nrows=1, ncols=1, figsize = (12, 5))
df1.rolling(24).mean().rename(columns={"count": "Month SMA"}).plot(ax=axes, lw=0.9)
plt.show()

# model
#creating train and test sets
dataset = df1.values

train = dataset[0:396,:]
valid = dataset[396:,:]


plt.plot(train)
plt.show()

plt.plot(valid)
plt.show()


#converting dataset into x_train and y_train
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

x_train, y_train = [], []
for i in range(60,len(train)):
    x_train.append(scaled_data[i-60:i,0])
    y_train.append(scaled_data[i,0])
x_train, y_train = np.array(x_train), np.array(y_train)
# x_train, y_train = [], []
# for i in range(60,len(train)):
#     x_train.append(scaled_data[i-60:i,0])
#     y_train.append(scaled_data[i,0])
# x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
x_train.shape

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)

#predicting 246 values, using past 60 from the train data
inputs = df1[len(df1) - len(valid) - 60:].values
inputs = inputs.reshape(-1,1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(60,inputs.shape[0]):
    X_test.append(inputs[i-60:i,0])
X_test = np.array(X_test)

X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
predicted_value = model.predict(X_test)
predicted_value = scaler.inverse_transform(predicted_value)

rmse=np.sqrt(np.mean(np.power((valid-predicted_value),2)))
rmse

mse=np.mean(np.power((valid-predicted_value), 2))
mse

mae=np.mean(np.abs(valid - predicted_value))
mae

#for plotting
train = df1[:396]
valid = df1[396:]
valid['Predictions'] = predicted_value
plt.plot(train['Pressure'])
plt.show()
plt.plot(valid[['Pressure','Predictions']])
plt.show()

df1.to_csv('mars_pressure.csv', header=True)