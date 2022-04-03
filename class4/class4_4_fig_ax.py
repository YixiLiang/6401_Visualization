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

fig = plt.figure(figsize=(16,8))
col2 = col.drop("Volume")

# df[col2].plot()
# plt.figure(figsize=(24,12))

fig, ax = plt.subplots(2,3,figsize=(16,8))
z = 0
for i in range(1,3):
    for j in range(1,4):
        ax[i-1,j-1].plot(df[col[z]])
        # ax[i-1,j-1].legend()
        ax[i-1,j-1].set_title(f'MSFT {col[z]}')
        ax[i-1,j-1].set_xlabel('Time')
        ax[i-1,j-1].set_ylabel('USD($)')
        ax[i-1,j-1].grid(axis = 'y')
        z += 1

plt.tight_layout()
plt.show()