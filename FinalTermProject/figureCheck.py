import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# pandas
df = pd.read_csv('weatherAUS.csv')
df_weather = df.copy()

# simplify dataset
df_figure = df_weather[
    ['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustDir',
     'WindGustSpeed', 'RainToday', 'RainTomorrow']].copy()
df_figure.dropna(how='any', inplace=True)
showFeature = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'RainTomorrow']
showCityName = ['Albury', 'BadgerysCreek', 'Cobar']
df_figure_city_time = df_figure[
    (df_figure['Date'] > '2017-01-01') & (df_figure['Location'].isin(showCityName))]
df_figure_city = df_figure[df_figure['Location'].isin(showCityName)]

# app = dash.Dash('figureCheck', external_stylesheets=external_stylesheets)

labels = df_figure_city_time['WindGustDir'].value_counts().keys().tolist()
values = df_figure_city_time['WindGustDir'].value_counts().tolist()
fig = px.pie(labels=['SE', 'SW', 'ENE', 'E', 'WSW', 'W', 'S', 'SSW', 'ESE', 'SSE', 'NE', 'NNE', 'WNW', 'N', 'NW', 'NNW'], values=values, title='Pie chart of the wind gust direction')
fig.show()

# app.layout([
#     figTabsA
# ])

# app.run_server(
#     port=8045,
#     debug=True
# )
