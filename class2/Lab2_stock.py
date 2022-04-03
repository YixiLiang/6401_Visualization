import pandas as pd
import pandas_datareader as web
import numpy as np


stocks = ["AAPL","ORCL","TSLA","IBM","YELP","MSFT"]
features= ["High", "Low", "Open", "Close", "Volume", "Adj Close"]
colunmsName = ["High($)", "Low($)", "Open($)", "Close($)", "Volume", "Adj Close($)"]
pd.options.display.float_format = "{:,.2f}".format
#######################################
#Q1 load data
#######################################
dfAAPL = web.DataReader("AAPL", data_source="yahoo", start="2000-01-01", end='2021-09-08')
dfORCL = web.DataReader("ORCL", data_source="yahoo", start="2000-01-01", end='2021-09-08')
dfTSLA = web.DataReader("TSLA", data_source="yahoo", start="2000-01-01", end='2021-09-08')
dfIBM = web.DataReader("IBM", data_source="yahoo", start="2000-01-01", end='2021-09-08')
dfYELP = web.DataReader("YELP", data_source="yahoo", start="2000-01-01", end='2021-09-08')
dfMSFT = web.DataReader("MSFT", data_source="yahoo", start="2000-01-01", end='2021-09-08')
# name = df.columns
# print(name)
# df.describe()

#######################################
#Q2 Mean Value comparison
#######################################
data = {
    "AAPL": np.around(np.mean(dfAAPL), 2),
    "ORCL": np.around(np.mean(dfORCL), 2),
    "TSLA": np.around(np.mean(dfTSLA), 2),
    "IBM": np.around(np.mean(dfIBM), 2),
    "YELP": np.around(np.mean(dfYELP), 2),
    "MSFT": np.around(np.mean(dfMSFT), 2)
}
# Create DataFrame
dfMean = pd.DataFrame(data)
dfMeanFinal = dfMean.copy()
# calculate the maximun and minimun of each row
dfMeanFinal["Maximum Value"] = dfMean.astype("float64").idxmax(axis=1)
dfMeanFinal["Minimum Value"] = dfMean.astype("float64").idxmin(axis=1)
# Matrix transpose
dfMeanFinal = dfMeanFinal.T
# Change columns' name
dfMeanFinal.columns = colunmsName
print("\nMean Value comparison: ")
print(dfMeanFinal)

#######################################
#Q3 Variance comparison
#######################################
data = {
    "AAPL": np.around(np.var(dfAAPL), 2),
    "ORCL": np.around(np.var(dfORCL), 2),
    "TSLA": np.around(np.var(dfTSLA), 2),
    "IBM": np.around(np.var(dfIBM), 2),
    "YELP": np.around(np.var(dfYELP), 2),
    "MSFT": np.around(np.var(dfMSFT), 2)
}
# Create DataFrame
dfVariance = pd.DataFrame(data)
dfVarianceFinal = dfVariance.copy()
# calculate the maximun and minimun of each row
dfVarianceFinal["Maximum Value"] = dfVariance.astype("float64").idxmax(axis=1)
dfVarianceFinal["Minimum Value"] = dfVariance.astype("float64").idxmin(axis=1)
# Matrix transpose
dfVarianceFinal = dfVarianceFinal.T
# Change columns' name
dfVarianceFinal.columns = colunmsName
print("\nVariance comparison:")
print(dfVarianceFinal)

#######################################
#Q4 Standard Deviation Value comparison
#######################################
data = {
    "AAPL": np.around(np.std(dfAAPL), 2),
    "ORCL": np.around(np.std(dfORCL), 2),
    "TSLA": np.around(np.std(dfTSLA), 2),
    "IBM": np.around(np.std(dfIBM), 2),
    "YELP": np.around(np.std(dfYELP), 2),
    "MSFT": np.around(np.std(dfMSFT), 2)
}
# Create DataFrame
dfStdDev = pd.DataFrame(data)
dfStdDevFinal = dfStdDev.copy()
# calculate the maximun and minimun of each row
dfStdDevFinal["Maximum Value"] = dfStdDev.astype("float64").idxmax(axis=1)
dfStdDevFinal["Minimum Value"] = dfStdDev.astype("float64").idxmin(axis=1)
# Matrix transpose
dfStdDevFinal = dfStdDevFinal.T
# Change columns' name
dfStdDevFinal.columns = colunmsName
print("\nStandard Deviation Value comparison: ")
print(dfStdDevFinal)

#######################################
#Q5 Median Value comparison
#######################################
# 使用df.median因为np.mean出来全部的中位数
data = {
    "AAPL": np.around(dfAAPL.median(axis=0), 2),
    "ORCL": np.around(dfORCL.median(axis=0), 2),
    "TSLA": np.around(dfTSLA.median(axis=0), 2),
    "IBM": np.around(dfIBM.median(axis=0), 2),
    "YELP": np.around(dfYELP.median(axis=0), 2),
    "MSFT": np.around(dfMSFT.median(axis=0), 2)
}
# Create DataFrame
dfMedian = pd.DataFrame(data)
dfMedianFinal = dfMedian.copy()
# calculate the maximun and minimun of each row
dfMedianFinal["Maximum Value"] = dfMedian.astype("float64").idxmax(axis=1)
dfMedianFinal["Minimum Value"] = dfMedian.astype("float64").idxmin(axis=1)
# Matrix transpose
dfMedianFinal = dfMedianFinal.T
# Change columns' name
dfMedianFinal.columns = colunmsName
print("\nMedian Value comparison:")
print(dfMedianFinal)

#######################################
#Q10
#######################################
print("\nCorrelation matrix for the Apple company:")
print(dfAAPL.corr())
print("\nCorrelation matrix for the ORCL company:")
print(dfORCL.corr())
print("\nCorrelation matrix for the TSLA company:")
print(dfTSLA.corr())
print("\nCorrelation matrix for the IBM company:")
print(dfIBM.corr())
print("\nCorrelation matrix for the YELP company:")
print(dfYELP.corr())
print("\nCorrelation matrix for the MSFT company:")
print(dfMSFT.corr())

# rename col
# df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
# df.rename(columns={"A": "a", "B": "c"})
