import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as web

plt.style.use('seaborn-deep')

df = web.DataReader("MSFT", data_source='yahoo', start = '2000-01-01', end='2022-02-02')
col = df.columns
print(col)

# plt.figure()
# plt.plot(df.Close, marker='.')
# plt.grid(axis='y')
# plt.show()

# plt.subplot(row, col, current)

plt.figure(figsize=(16,8))
plt.subplot(2,3,1)
plt.plot(df.High)
plt.title("MSFT High")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2,3,2)
plt.plot(df.Low)
plt.title("MSFT Low")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2,3,3)
plt.plot(df.Open)
plt.title("MSFT Open")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2,3,4)
plt.plot(df.Close)
plt.title("MSFT Close")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2,3,5)
plt.plot(df.Volume)
plt.title("MSFT Volume")
plt.xlabel("Time")
plt.ylabel("Quntity")
# plt.yscale("log")
# plt.yscale('linear') #default
plt.grid(axis='y')

plt.subplot(2,3,6)
plt.plot(df['Adj Close'].values)
plt.title("MSFT Adj Close")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.tight_layout() #fix overlapping
plt.show()


