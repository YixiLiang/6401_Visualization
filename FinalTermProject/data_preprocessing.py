import pandas as pd
import numpy as np
import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


#######################################
# load data
#######################################
df = pd.read_csv('weatherAUS.csv')
df_weather = df.copy()
colName = df_weather.columns
largeNaList = []
for i in range(len(colName)):
    columnName = colName[i]
    naPercentage = df_weather.isna().sum()[columnName] / len(df_weather[columnName])
    if naPercentage > 0.2:
        largeNaList.append(columnName + ': ' + str(naPercentage * 100) + '%')

# print(largeNaList)
# df_weather.fillna(value=df_weather.mean(), inplace=True)

df_weather["RainToday"] = np.where(df_weather["RainToday"] == "No", 0, 1)
df_weather['Date'] = pd.to_datetime(df_weather['Date'], format='%Y-%m-%d')
# get all the city name
cityName = df_weather['Location'].unique()
# make a list to store cityName
cityNameDropdownOptions = []
for i in range(len(cityName)):
    dic = {'label': cityName[i], 'value': cityName[i]}
    cityNameDropdownOptions.append(dic)

# get all the year
dateYear = [df_weather['Date'][i].year for i in range(len(df_weather['Date']))]
dateYear = np.unique(dateYear)
# get start date and end date
minDate = min(df_weather['Date'])
maxDate = max(df_weather['Date'])


#######################################
#
#######################################
