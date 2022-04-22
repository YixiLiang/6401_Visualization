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
df_core_component = df_weather[['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed']]
showCityName = ['Albury', 'BadgerysCreek', 'Cobar']
df_core_component_city_time = df_core_component[
    (df_core_component['Date'] > '2017-01-01') & (df_core_component['Location'].isin(showCityName))]
df_core_component_city = df_core_component[df_core_component['Location'].isin(showCityName)]

# app = dash.Dash('figureCheck', external_stylesheets=external_stylesheets)

df_core_component_city_rangeSlider = df_core_component_city[
    (df_core_component_city['Date'] > '2015') & (df_core_component_city['Date']) < '2017']
fig = px.line(data_frame=df_core_component_city, x='Date', y='MaxTemp', color='Location',
              title=f'Line plot of MaxTemp from {2015} to {2017}')
fig.show()

# app.layout([
#     figTabsA
# ])

# app.run_server(
#     port=8045,
#     debug=True
# )
