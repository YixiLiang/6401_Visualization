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

dfMean = np.mean(dfAAPL)
dfMeanSec = pd.DataFrame(columns=colunmsName)
listAAPL = []
listORCL = []
listTSLA = []
listIBM = []
listYELP = []
listMSFT = []

for i in dfAAPL.columns:
    listAAPL.append(np.mean(dfAAPL[i]))
    listORCL.append(np.mean(dfORCL[i]))
    listTSLA.append(np.mean(dfTSLA[i]))
    listIBM.append(np.mean(dfIBM[i]))
    listYELP.append(np.mean(dfYELP[i]))
    listMSFT.append(np.mean(dfMSFT[i]))

dfMeanSec.loc['AAPL',:] = listAAPL
dfMeanSec.loc['ORCL',:] = listORCL
dfMeanSec.loc['TSLA',:] = listTSLA
dfMeanSec.loc['IBM',:] = listIBM
dfMeanSec.loc['YELP',:] = listYELP
dfMeanSec.loc['MSFT',:] = listMSFT
dfMeanFinal = dfMeanSec.copy()

# listTest = list[1,2,3,4,5,6]
dfMeanFinal.loc['Maximum Value',:] = dfMeanSec.astype('float64').idxmax(axis=0)
dfMeanFinal.loc['Minimum Value',:] = dfMeanSec.astype('float64').idxmin(axis=0)
# dfMeanSec.loc['Maximum Value',:] = dfMeanSec.idxmax(axis=0).to_numpy()
# dfMeanSec.loc['Minimum Value',:] = dfMeanSec.idxmin(axis=0)
# dfMeanSec.append(, )







