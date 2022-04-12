import pandas as pd
import numpy as np
import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

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

# df_weather["RainToday"] = np.where(df_weather["RainToday"] == "No", 0, 1)
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
# city section
#######################################

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

# page layout
city_page = html.Div([
    html.Div(className='container', children=[
        html.H6("Hello"),
        city_input,
        date_input,
        submit_date,
        # dcc.Graph('Temperature-lineplot'),
        html.Div(id='Temperature-lineplot'),
    ])
])


@app.callback(
    Output(component_id='Temperature-lineplot', component_property='children'),
    [Input(component_id='submit_date', component_property='n_clicks')],
    [State(component_id='cityName', component_property='value'),
     State(component_id='date', component_property='start_date'),
     State(component_id='date', component_property='end_date')]
)
def display_city_Temp(clicks, cityName, start_date, end_date):
    figTemp = go.Figure()
    figRainfall = go.Figure()
    figWindGustDir = go.Figure()
    figWindGustSpeed = go.Figure()
    figRainToday = go.Figure()
    if clicks is not None:
        # figure about MinTemp and MaxTemp
        figTemp.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                        df_weather['Date'] <= end_date)][
            'MinTemp'],
                                     mode='lines',
                                     name='MinTemp'))
        figTemp.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                        df_weather['Date'] <= end_date)][
            'MaxTemp'],
                                     mode='lines',
                                     name='MaxTemp')),

        figTemp.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                    df_weather['Date'] <= end_date)][
            'Temp9am'],
                                     mode='lines',
                                     name='Temp9am')),
        figTemp.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                    df_weather['Date'] <= end_date)][
            'Temp3pm'],
                                     mode='lines',
                                     name='Temp3pm')),

        figTemp.update_layout(title=f'Highest and Lowest Temperatures in {cityName}',
                              xaxis_title='Date',
                              yaxis_title='Temperature (degrees C)')
        # figure about Rainfall
        figRainfall.add_trace(go.Violin(y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                        df_weather['Date'] <= end_date)]['Rainfall'], box_visible=True, line_color='black',
                                        meanline_visible=True, fillcolor='lightseagreen', opacity=0.6,
                                        x0='rainfall'))
        figRainfall.update_layout(title=f'Violin of Rain fall in{cityName}')
        # figure about Wind Gust Direction
        labels = df_weather[(df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                    df_weather['Date'] <= end_date)]['WindGustDir'].value_counts().keys().tolist()
        values = df_weather[(df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                    df_weather['Date'] <= end_date)]['WindGustDir'].value_counts().tolist()
        figWindGustDir.add_trace(go.Pie(labels=labels, values=values))
        figWindGustDir.update_layout(title=f'Pie plot of wind direction in {cityName}')
        # figure about Wind Gust Speed
        figWindGustSpeed.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                        df_weather['Date'] <= end_date)]['WindGustSpeed'],
                                              mode='lines',
                                            name='WindGustSpeed'))
        figWindGustSpeed.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                    df_weather['Date'] <= end_date)]['WindSpeed9am'],
                                              mode='lines',
                                              name='WindSpeed9am'
                                              ))
        figWindGustSpeed.add_trace(go.Scatter(x=df_weather['Date'], y=df_weather[
            (df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                    df_weather['Date'] <= end_date)]['WindSpeed3pm'],
                                              mode='lines',
                                              name='WindSpeed3pm'
                                              ))



        figWindGustSpeed.update_layout(title=f'Line plot of wind speed in {cityName}')
        # figure about Rain Today
        labels = df_weather[(df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                df_weather['Date'] <= end_date)]['RainToday'].value_counts().keys().tolist()
        values = df_weather[(df_weather['Location'] == cityName) & (df_weather['Date'] >= start_date) & (
                df_weather['Date'] <= end_date)]['RainToday'].value_counts().tolist()
        figRainToday.add_trace(go.Pie(labels=labels, values=values))
        figRainToday.update_layout(title=f'Pie plot of rain today in {cityName}')


    city_content_layout = html.Div([
        dbc.Row(dbc.Col(dcc.Graph(figure=figTemp))),
        dbc.Row(dbc.Col(dcc.Graph(figure=figRainfall))),
        dbc.Row(dbc.Col(dcc.Graph(figure=figWindGustDir))),
        dbc.Row(dbc.Col(dcc.Graph(figure=figWindGustSpeed))),
        dbc.Row(dbc.Col(dcc.Graph(figure=figRainToday))),
    ])

    return city_content_layout


#######################################
# index-page
#######################################


nav = dbc.Nav(
    [
        dcc.Location(id='url', refresh=False),
        dbc.NavItem(dbc.NavLink("City", id='city-page', active=True, href="/city-page")),
        dbc.NavItem(dbc.NavLink("Temperature", href="#")),
        dbc.NavItem(dbc.NavLink("Rain", href="#")),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
            label="Dropdown",
            nav=True,
        ),
    ]
)


@app.callback(
    Output(component_id='page-main-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def navLink(pathname):
    if pathname == '/city-page':
        return city_page
    else:
        return index_page_main


# this example that adds a logo to the navbar brand
logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url('kangaroo.jpg'),
                                         style={'border-radius': '5px', 'margin-right': '10px'}, height="40px",
                                         width="40px")),
                        dbc.Col(dbc.NavbarBrand(
                            children=[html.Font('Rain in Australia', className='fs-6', style={'font-style': 'italic'})],
                            className='ms-2')),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            nav,
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="dark",
    dark=True,
    className="mb-4",
    style={'margin-bottom': "0"}
)

carousel = dbc.Carousel(
    items=[
        {"key": "1",
         "src": 'https://images.pexels.com/photos/2845013/pexels-photo-2845013.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
         "header": "People Gathering Outside Sydney Opera House",
         "caption": 'Sydney, NSW, Australia',
         "imgClassName": 'index-img'
         },
        {"key": "2",
         "src": "https://images.pexels.com/photos/995764/pexels-photo-995764.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "Aerial View of Sydney",
         "caption": 'Mosman, NSW, Australia',
         "imgClassName": 'index-img'
         },
        {"key": "3",
         "src": "https://images.pexels.com/photos/533509/pexels-photo-533509.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "Group of People on Body of Water",
         "imgClassName": 'index-img'
         },
        {"key": "4",
         "src": "https://images.pexels.com/photos/513799/pexels-photo-513799.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "High Rise Buildings",
         "imgClassName": 'index-img'
         },
        {"key": "5",
         "src": "https://images.pexels.com/photos/2476154/pexels-photo-2476154.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "Close-Up Photo of Grass During Golden Hour",
         "caption": 'Surfers Paradise, QLD, Australia',
         "imgClassName": 'index-img'

         },
    ],
    controls=True,
    indicators=True,
    interval=5000,
    ride="carousel",
    style={'margin': '0px 150px 0px 150px'}
)
index_page_main = html.Div([
    html.Div(className='container', children=[
        dbc.Row(
            dbc.Col(
                html.Div('Rain in Australia', id='homePage-title'),
            )
        ),
        dbc.Row(
            dbc.Col(
                carousel
            )
        ),

        dbc.Row(dbc.Col(html.Hr(style={'color': 'gary', 'background-color': 'gary', 'height': '1px'}))),
        html.Div(id='main-content', children=[
            dbc.Row([
                dbc.Col(html.Div([html.P("About Dataset", className='h3')]), width="auto"),
                dbc.Col(html.Div(children=[
                    html.I(className='bi bi-box-arrow-up-right',
                           style={'margin-right': '10px', 'text-align': 'left',
                                  'line-height': '34px'}),
                    html.A(href='https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package', children=[
                        html.Img(src='https://www.kaggle.com/static/images/site-logo.svg',
                                 style={'height': '34px', 'width': '70px'})
                    ], style={'text-align': 'left'})
                ]))
            ]),
            dbc.Row(dbc.Col(html.Div([html.P("Context", className='h4')]))),
            dbc.Row(dbc.Col(html.Div([html.P(className='text-muted', children=
            "Predict next-day rain by training classification models on the target variable RainTomorrow.")]))),
            dbc.Row(dbc.Col(html.Div([html.P("Content", className='h4')]))),
            dbc.Row(dbc.Col(html.Div([html.P(className='text-muted', children=
            "This dataset contains about 10 years of daily weather observations from many locations across Australia.")]))),
            dbc.Row(dbc.Col(html.Div([html.P(className='text-muted', children=
            "RainTomorrow is the target variable to predict. It means -- did it rain the next day, Yes or No? This column is Yes if the rain for that day was 1mm or more.")]))),
            dbc.Row(dbc.Col(html.Div([html.P("Source & Acknowledgements", className='h4')]))),
            dbc.Row(dbc.Col(html.Div([
                html.P(className='list-inline-item', children=
                "Observations were drawn from numerous weather stations. The daily observations are available from:"),
                html.A('http://www.bom.gov.au/climate/data', href='http://www.bom.gov.au/climate/data')
            ]))),
            dbc.Row(dbc.Col(html.Div([
                html.P(className='list-inline-item', children="An example of latest weather observations in Canberra:"),
                html.A('http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml',
                       href='http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml')
            ]))),
            dbc.Row(dbc.Col(html.Div([
                html.P(className='list-inline-item', children="Definitions adapted from"),
                html.A('http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml',
                       href='http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml')
            ]))),
            dbc.Row(dbc.Col(html.Div(children=[
                html.P(className='list-inline-item', children="Data source: "),
                html.A('http://www.bom.gov.au/climate/dwo/', href='http://www.bom.gov.au/climate/dwo/'),
                html.P(className='list-inline-item', children=" and "),
                html.A('http://www.bom.gov.au/climate/data', href='http://www.bom.gov.au/climate/data'),
            ]))),
            dbc.Row(dbc.Col(html.Div(
                [html.Font("Copyright Commonwealth of Australia 2010, Bureau of Meteorology.",
                           style={'color': 'gary'})])))
        ]),

    ])
])

index_page_footer = html.Footer(id='index-Page-footer', children=[
    html.Div(className='container', children=[
        html.P('Powered by Yixi Liang', className='text-muted')
    ])
])

index_page = html.Div(children=[
    # html.Div(className='bg-test'),
    logo,

    html.Div(id='page-main-content', children=[
        index_page_main,
    ]),
    index_page_footer

], className='bg-test')

app.layout = html.Div(
    [index_page]
)

app.run_server(
    port=8033,
    debug=True
)
