import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as web

plt.style.use('seaborn-deep')

# df = web.DataReader("MSFT", data_source='yahoo', start = '2000-01-01', end='2022-02-02')
# col = df.columns
#
# correlation = df.corr()
# print(correlation)
# plt.hexbin(df.Volume.values, df.Open.values, gridsize=(50,50))
np.random.seed(123)
x = np.random.normal(size=5000)
y = 2*x + np.random.normal(size=5000)

plt.figure(figsize=(16,8))
plt.hexbin(x,y,gridsize=(50,50))
plt.xlabel("Random variable x", fontsize = 20)
plt.ylabel("Random variable y", fontsize = 20)
plt.title("Hexbin plot between Normal Random variables",fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.savefig('Test.pdf', dpi = 600)
plt.show()
# plt.savefig
# • dpi
# • metadata : ’png’, ’pdf’,
# ’svg’,’eps’
# • bbox inches : bounding box
# in inches, save only portion
# of the figure
# • pad inches : amount of
# padding around the figure
# • facecolor
# • edgecolor
# • backend: for rendering
# • orientation : ’land-
# scape’,’portrait’
# • papertype
# • transparent : True or Fales


