import pandas as pd
import numpy as np
import plotly.express as px


#######################################
# load data
#######################################
df = pd.read_csv('weatherAUS.csv')
# print(df.describe())
print(df.isna().sum())
# df.dropna(how='any', inplace=True)
# print(df.isna().sum())
df_weather = df.copy()
colName = df_weather.columns
largeNaList =[]
for i in range(len(colName)):
    columnName = colName[i]
    naPercentage = df_weather.isna().sum()[columnName]/len(df_weather[columnName])
    if naPercentage > 0:
        largeNaList.append(columnName + ': '+ str(naPercentage * 100) + '%')

print(largeNaList)
df_weather.fillna(value=df_weather.mean(), inplace=True)

df_weather["RainToday"] = np.where(df_weather["RainToday"] == "No", 0, 1)

#######################################
#
#######################################
# lineplot
# fig = px.line(df_weather,'Date','MaxTemp',color='Location')
# fig.show()

#barplot
# city = df_weather['Location'].unique()
# fig = px.bar(data_frame=df_weather, x='Location')
# fig.show()
#histogram
fig = px.histogram(data_frame=df_weather, x='Location',color='RainToday', marginal='violin')
fig.show()

df_city = df_weather[df_weather['Location'] == 'Albury']

fig = px.histogram(df_city, x='WindGustDir')
fig.show()