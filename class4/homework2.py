import pandas as pd
import pandas_datareader as web
from datetime import date
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

#######################################
# Q1 load data
#######################################
stocks = ['AAPL', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT']
# today = date.today()
# end defualt is today
dfAAPL = web.DataReader('AAPL', data_source='yahoo', start='2000-01-01')
dfORCL = web.DataReader("ORCL", data_source="yahoo", start="2000-01-01")
dfTSLA = web.DataReader("TSLA", data_source="yahoo", start="2000-01-01")
dfIBM = web.DataReader("IBM", data_source="yahoo", start="2000-01-01")
dfYELP = web.DataReader("YELP", data_source="yahoo", start="2000-01-01")
dfMSFT = web.DataReader("MSFT", data_source="yahoo", start="2000-01-01")
df = [dfAAPL, dfORCL, dfTSLA, dfIBM, dfYELP, dfMSFT]
col = dfAAPL.columns
#######################################
# Q2 + Q3 lineplot of all features of six companies
#######################################
# outer loop is looping six features of the companies, inner loop is looping companies
for i in range(6):
    plt.figure(figsize=(16, 8))
    for j in range(6):
        plt.subplot(3, 2, j + 1)
        plt.plot(df[j][col[i]])
        if col[i] != 'Volume':
            plt.title(f'{col[i]} price history of {stocks[j]}')
        else:
            plt.title(f'Volume history of {stocks[j]}')
        plt.xlabel("Time")
        if col[i] != 'Volume':
            plt.ylabel(f'{col[i]} price USD($)')
        else:
            plt.ylabel('Quantity')
        plt.grid()
    plt.tight_layout()
    plt.show()
#######################################
# Q4 + Q5 histogram of all features of six companies
#######################################
# outer loop is looping six features of the companies, inner loop is looping companies
for i in range(6):
    plt.figure(figsize=(16, 8))
    for j in range(6):
        plt.subplot(3, 2, j + 1)
        plt.hist(df[j][col[i]], bins=50)
        if col[i] != 'Volume':
            plt.title(f'{col[i]} price history of {stocks[j]}')
        else:
            plt.title(f'Volume history of {stocks[j]}')

        if col[i] != 'Volume':
            plt.xlabel('Value in USD($)')
        else:
            plt.xlabel('Quantity')
        plt.ylabel("Frequency")
        # plt.legend()
        plt.grid()
    plt.tight_layout()
    plt.show()
#######################################
# Q6 + Q7 correlation coefficients
#######################################
# # AAPL
# print(f'The person correlation coefficients between all 6 features for the “{stocks[0]}” company')
# corCoeAAPL = df[0].corr()
# print(corCoeAAPL)
# print('Each feature have the highest correlation coefficient with themselves.')
# print('Volume and Adj Close have the lowest correlation coefficient')
# # ORCL
# print(f'The person correlation coefficients between all 6 features for the “{stocks[1]}” company')
# corCoeORCL = df[1].corr()
# print(corCoeORCL)
# print('Each feature have the highest correlation coefficient with themselves.')
# print('Volume and High have the lowest correlation coefficient')
# # TSLA
# print(f'The person correlation coefficients between all 6 features for the “{stocks[2]}” company')
# corCoeTSLA = df[2].corr()
# print(corCoeTSLA)
# print('Each feature have the highest correlation coefficient with themselves.')
# print('Volume and Low have the lowest correlation coefficient')
# # IBM
# print(f'The person correlation coefficients between all 6 features for the “{stocks[3]}” company')
# corCoeIBM = df[3].corr()
# print(corCoeIBM)
# print('Each feature have the highest correlation coefficient with themselves.')
# print('Volume and High have the lowest correlation coefficient')
# # YELP
# print(f'The person correlation coefficients between all 6 features for the “{stocks[4]}” company')
# corCoeYELP = df[4].corr()
# print(corCoeYELP)
# print('Each feature have the highest correlation coefficient with themselves.')
# print('Volume and Low have the lowest correlation coefficient')
# # MSFT
# print(f'The person correlation coefficients between all 6 features for the “{stocks[5]}” company')
# corCoeMSFT = df[5].corr()
# print(corCoeMSFT)
# print('Each feature have the highest correlation coefficient with themselves.')
# print('Volume and High have the lowest correlation coefficient')
#

corCoeList = []
for i in range(6):
    print(f'The person correlation coefficients between all 6 features for the “{stocks[i]}” company')
    corCoe = df[i].corr()
    print(corCoe)
    corCoe1 = corCoe.copy()
    corCoe2 = corCoe.copy()
    # high
    corCoe1 = corCoe1.replace(1, 0)
    firstHigh = corCoe1.abs().idxmax().max()
    secondHigh = corCoe1.abs().idxmax()[firstHigh]
    # low
    firstLow = corCoe2.abs().idxmin().min()
    secondLow = corCoe2.abs().idxmin()[firstLow]
    print(f'{firstHigh} and {secondHigh} have the highest correlation coefficient.')
    print(f'{firstLow} and {secondLow} have the lowest correlation coefficient.')
    corCoeList.append(corCoe)
#######################################
# Q8 + Q9 correlation coefficients
#######################################
# corCoeList = [corCoeAAPL, corCoeORCL, corCoeTSLA, corCoeIBM, corCoeYELP, corCoeMSFT]
for k in range(6):
    plt.figure(figsize=(16, 16))
    for i in range(6):
        for j in range(6):
            plt.subplot(6, 6, i * 6 + j + 1)
            plt.scatter(df[k][col[j]], df[k][col[i]])
            # corr,_ = pearsonr(df[k][col[j]], df[k][col[i]])
            # plt.title(f"r = {corr:.2f}")
            plt.title(f"r = {corCoeList[k].iloc[i, j]:.2f}")
            plt.xlabel(f'{col[j]} ($)')
            plt.ylabel(f'{col[i]} ($)')
            plt.grid()
    plt.tight_layout()
    plt.show()
#######################################
# Q10 scatter matrix
#######################################
plt.figure(figsize=(16, 16))
pd.plotting.scatter_matrix(dfAAPL, alpha=0.5, s=10, diagonal='kde', hist_kwds={'bins': 50})
plt.tight_layout()
plt.show()
