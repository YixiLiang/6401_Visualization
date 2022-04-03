import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as web

plt.style.use('seaborn-deep')

df = web.DataReader("MSFT", data_source='yahoo', start='2000-01-01', end='2022-02-02')
col = df.columns
print(col)

plt.figure()
plt.plot(df.Close, marker='.')
plt.grid(axis='y')
plt.show()

fig = plt.figure(figsize=(16, 8))
for i in range(6):
    ax1 = fig.add_subplot(2, 3, i + 1)
    ax1.plot(df[col[i]])
    ax1.set_title(f"MSFT {col[i]} stock", fontsize=15)
    ax1.set_xlabel("Time123", fontsize=15)
    if col[i] == 'Volume':
        ax1.set_ylabel("Quntity", fontsize=15)
    else:
        ax1.set_ylabel("USD($)", fontsize=15)
    ax1.set_font = 20
    plt.grid(b=True, axis='y')
plt.tight_layout()
plt.show()
# ax.set_ylabel(r'$ {y} = {10}^* $')
# label = '$f(x) = \sqrt{x}$'
plt.figure(figsize=(16, 8))
plt.subplot(2, 3, 1)
plt.plot(df.High)
plt.title("MSFT High")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2, 3, 2)
plt.plot(df.Low)
plt.title("MSFT Low")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2, 3, 3)
plt.plot(df.Open)
plt.title("MSFT Open")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2, 3, 4)
plt.plot(df.Close)
plt.title("MSFT Close")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')

plt.subplot(2, 3, 5)
plt.plot(df.Volume)
plt.title("MSFT Volume")
plt.xlabel("Time")
plt.ylabel("Quntity")
plt.grid(axis='y')

plt.subplot(2, 3, 6)
plt.plot(df['Adj Close'])
plt.title("MSFT Adj Close")
plt.xlabel("Time")
plt.ylabel("USD($)")
plt.grid(axis='y')
plt.tight_layout()  # fix overlapping
plt.show()

# diagonal {‘hist’, ‘kde’} /

pd.plotting.scatter_matrix(df, diagonal='hist', hist_kwds={'bins': 50},figsize=(16,8))
plt.tight_layout()  # fix overlapping
plt.show()

# frameDataFrame
# alpha float, optional
# Amount of transparency applied.
#
# figsize   (float,float), optional
# A tuple (width, height) in inches.
#
# ax    Matplotlib axis object, optional
# gridbool, optional
# Setting this to True will show the grid.
#
# diagonal{‘hist’, ‘kde’}
# Pick between ‘kde’ and ‘hist’ for either Kernel Density Estimation or Histogram plot in the diagonal.
#
# marker    str, optional
# Matplotlib marker type, default ‘.’.
#
# density_kwds  keywords
# Keyword arguments to be passed to kernel density estimate plot.
#
# hist_kwds keywords
# Keyword arguments to be passed to hist function.
#
# range_padding float, default 0.05
# Relative extension of axis range in x and y with respect to (x_max - x_min) or (y_max - y_min).
