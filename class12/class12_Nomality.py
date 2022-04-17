import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt

stocks = ['AAPL', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT']
df = web.DataReader("AAPL", data_source='yahoo', start = '2000-01-01', end='2022-04-13')

df[['Close','Volume']].plot()
plt.show()

close = df['Close'].values
volume = df['Volume'].values

close_z = (close - np.mean(close))/np.std(close)
volume_z = (volume - np.mean(volume))/np.std(volume)

plt.figure()
plt.plot(df.index, close_z, label = 'close')
plt.plot(df.index, volume_z, label = 'volume')

plt.legend()
plt.show()

# y = np.array([1,3,5,4,7,9])
#
# mean_y = np.mean(y)
# std = np.std(y)
#
# z = (y-mean_y)/std
# print(z)



