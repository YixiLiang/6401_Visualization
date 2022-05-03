import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# pandas
df = pd.read_csv('../FinalTermProject/weatherAUS.csv')
df_weather = df.copy()
df_figure = df_weather.copy()
# simplify dataset
# df_figure = df_weather[
#     ['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustDir',
#      'WindGustSpeed', 'RainToday', 'RainTomorrow']].copy()
# df_figure.dropna(how='any', inplace=True)
# showFeature = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'RainTomorrow']
showCityName = ['Albury', 'BadgerysCreek', 'Cobar']
df_figure_city_time = df_figure[
    (df_figure['Date'] > '2017-01-01') & (df_figure['Location'].isin(showCityName))]
df_figure_city = df_figure[df_figure['Location'].isin(showCityName)]

# app = dash.Dash('figureCheck', external_stylesheets=external_stylesheets)

figCatplot = px.scatter(data_frame=df_figure_city_time, y='MaxTemp', x='Location', size='Rainfall',
                                color='Location',
                                title='Cat-plot of MaxTemp size by rainfall hue city')
figCatplot.update_layout(yaxis_title='MaxTemp (℃)')
figCatplot.show()


# app.layout([
#     figTabsA
# ])

# app.run_server(
#     port=8045,
#     debug=True
# )
