from datetime import date
from datetime import datetime
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
df = pd.read_csv('../FinalTermProject/weatherAUS.csv')
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
yearDropdownOptions = []
for i in range(len(cityName)):
    dic = {'label': cityName[i], 'value': cityName[i]}
    yearDropdownOptions.append(dic)
# get all the year
dateYear = [df_weather['Date'][i].year for i in range(len(df_weather['Date']))]
dateYear = np.unique(dateYear)
# get start date and end date
minDate = min(df_weather['Date'])
maxDate = max(df_weather['Date'])

#######################################
#
#######################################

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(external_stylesheets=external_stylesheets)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

city_input = dbc.Row(
    [
        dbc.Label("City", width=1),
        dbc.Col(
            dcc.Dropdown(id='cityName',
                         options=cityNameDropdownOptions),
        ),
    ],
    className="mb-3",
)

date_input = dbc.Row(
    [
        dbc.Label("Date", width=1),
        dbc.Col(
            dcc.DatePickerRange(id='date',
                                min_date_allowed=minDate,
                                max_date_allowed=maxDate,
                                start_date=minDate,
                                end_date=maxDate,
                                display_format='Y-M-D',
                                start_date_placeholder_text='Y-M-D'
                                ),
        ),
    ],
    className="mb-3",
)

submit_date = dbc.Row(
    [
        dbc.Col(
            dbc.Button("Submit", id='submit_date', color="primary"), width="auto"
        ),
    ],
    className="mb-3",
)

# form = dbc.Form([city_input, date_input, submit_date])

app.layout = html.Div([
    # dcc.Dropdown(id='cityName',
    #              options=cityNameDropdownOptions,
    #              className="mb-3"),
    # # dcc.DatePickerRange(id='dateYear',
    # #              options=cityNameDropdownOptions,
    # #              className="mb-3"),
    # dcc.DatePickerRange(id='date',
    #                     start_date=minDate,
    #                     end_date=maxDate,
    #                     display_format='Y-M-D',
    #                     start_date_placeholder_text='Y-M-D'
    #                     ),
    html.H6("Hello"),
    city_input,
    date_input,
    submit_date,
    dcc.Graph('Temperature-lineplot'),

])


@app.callback(
    Output(component_id='Temperature-lineplot', component_property='figure'),
    [Input(component_id='submit_date', component_property='n_clicks')],
    [State(component_id='cityName', component_property='value'),
     State(component_id='date', component_property='start_date'),
     State(component_id='date', component_property='end_date')]
)
def display_city_Temp(clicks, cityName, start_date, end_date):

    fig = go.Figure()
    if clicks is not None:
        fig.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (df_weather['Date'] <= end_date)][
            'MinTemp'],
                                 mode='lines',
                                 name='MinTemp'))
        fig.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (df_weather['Date'] <= end_date)][
            'MaxTemp'],
                                 mode='lines',
                                 name='MaxTemp'))
        fig.update_layout(title=f'Highest and Lowest Temperatures in {cityName}',
                          xaxis_title='Date',
                          yaxis_title='Temperature (degrees C)')
    return fig



app.run_server(
    port=8039,
    debug=True
)

# lineplot
# fig = px.line(df_weather,'Date','MaxTemp',color='Location')
# fig.show()

# barplot
# city = df_weather['Location'].unique()
# fig = px.bar(data_frame=df_weather, x='Location')
# fig.show()
# histogram
# fig = px.histogram(data_frame=df_weather, x='Location',color='RainToday', marginal='violin')
# fig.show()
#
# df_city = df_weather[df_weather['Location'] == 'Albury']
#
# fig = px.histogram(df_city, x='WindGustDir')
# fig.show()
