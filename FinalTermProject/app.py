import pandas as pd
import numpy as np
import dash as dash
from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import datetime
import io
import base64
import plotly.figure_factory as ff

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])
server = app.server
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
        html.Div(
            html.P('Please select city and choose the date range, and press submit to see the result', className='h2')),
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

    df_display_city = df_weather[(df_weather['Date'] >= start_date) & (df_weather['Date'] <= end_date)]
    df_display_city = df_display_city[df_display_city['Location'] == cityName]
    if clicks is not None:
        # figTemp figure about MinTemp and MaxTemp
        figTemp.add_trace(go.Scatter(
            x=df_display_city['Date'],
            y=df_display_city['MinTemp'],
            mode='lines',
            name='MinTemp'))

        figTemp.add_trace(go.Scatter(
            x=df_display_city['Date'],
            y=df_display_city['MaxTemp'],
            mode='lines',
            name='MaxTemp'))

        figTemp.add_trace(go.Scatter(
            x=df_display_city['Date'],
            y=df_display_city['Temp9am'],
            mode='lines',
            name='Temp9am'))

        figTemp.add_trace(go.Scatter(
            x=df_display_city['Date'],
            y=df_display_city['Temp3pm'],
            mode='lines',
            name='Temp3pm'))

        figTemp.update_layout(title=f'Highest and Lowest Temperatures in {cityName}',
                              xaxis_title='Date',
                              yaxis_title='Temperature (degrees C)')

        # figRainfall figure about Rainfall
        figRainfall.add_trace(go.Violin(y=df_display_city['Rainfall'], box_visible=True, line_color='black',
                                        meanline_visible=True, fillcolor='lightseagreen', opacity=0.6,
                                        x0='rainfall'))
        figRainfall.update_layout(title=f'Violin of Rain fall in{cityName}')

        # figWindGustDir figure about Wind Gust Direction
        labels = df_display_city['WindGustDir'].value_counts().keys().tolist()
        values = df_display_city['WindGustDir'].value_counts().tolist()
        figWindGustDir.add_trace(go.Pie(labels=labels, values=values))
        figWindGustDir.update_layout(title=f'Pie plot of wind direction in {cityName}')

        # figure about Wind Gust Speed
        figWindGustSpeed.add_trace(go.Scatter(
            x=df_display_city['Date'],
            y=df_display_city['WindGustSpeed'],
            mode='lines',
            name='WindGustSpeed'))

        figWindGustSpeed.add_trace(go.Scatter(
            x=df_display_city['Date'],
            y=df_display_city['WindSpeed9am'],
            mode='lines',
            name='WindSpeed9am'))

        figWindGustSpeed.add_trace(go.Scatter(
            x=df_display_city['Date'],
            y=df_display_city['WindSpeed3pm'],
            mode='lines',
            name='WindSpeed3pm'))

        figWindGustSpeed.update_layout(title=f'Line plot of wind speed in {cityName}',
                                       yaxis_title='Wind Speed (km/h) ',
                                       xaxis_title='Date')

        # figure about Rain Today
        labels = df_display_city['RainToday'].value_counts().keys().tolist()
        values = df_display_city['RainToday'].value_counts().tolist()
        figRainToday.add_trace(go.Pie(labels=labels, values=values))
        figRainToday.update_layout(title=f'Pie plot of rain today in {cityName}',
                                   yaxis_title='Rainfall (mm)')

    city_content_layout = html.Div([
        html.Div(html.P('Line - plot', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figTemp))),
        html.Div(html.P('Violin - plot', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figRainfall))),
        html.Div(html.P('Pie - plot', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figWindGustDir))),
        html.Div(html.P('Line - plot', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figWindGustSpeed))),
        html.Div(html.P('Pie - plot', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figRainToday))),
    ])

    return city_content_layout
#######################################
# core_component section
#######################################
# simplify dataset
df_core_component = df_weather[['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed']]
showFeature = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed']
showCityName = ['Albury', 'BadgerysCreek', 'Cobar']
df_core_component_city_time = df_core_component[
    (df_core_component['Date'] > '2017-01-01') & (df_core_component['Location'].isin(showCityName))]
df_core_component_city = df_core_component[df_core_component['Location'].isin(showCityName)]
# dropdown menu options
showCityNameDropdownOptions = []
for i in range(len(showCityName)):
    dic = {'label': showCityName[i], 'value': showCityName[i]}
    showCityNameDropdownOptions.append(dic)
# feature options
showFeatureOptions = []
for i in range(len(showFeature)):
    dic = {'label': showFeature[i], 'value': showFeature[i]}
    showFeatureOptions.append(dic)
#######################################
# Tabs + check box + Multiple Division

tabs_layout = html.Div([
    html.Div(html.P('Multiple Tabs + Check box + Multiple Division', className='h2')),
    dbc.Tabs(
        [
            dbc.Tab(label=showFeature[0], tab_id=showFeature[0]),
            dbc.Tab(label=showFeature[1], tab_id=showFeature[1]),
            dbc.Tab(label=showFeature[2], tab_id=showFeature[2]),
            dbc.Tab(label=showFeature[3], tab_id=showFeature[3]),
        ],
        id='tabs',
        active_tab=showFeature[0]
    ),
    dcc.Checklist(
        id='checkbox_core',
        options=showCityNameDropdownOptions,
        value=[showCityName[0]]
    ),
    dcc.Graph(id='tabs_graph')
], className='core-component-section')

@app.callback(
    Output(component_id="tabs_graph", component_property='figure'),
    [Input(component_id='tabs', component_property='active_tab'),
     Input(component_id='checkbox_core', component_property='value')]
)
def switch_tab(featureName, cityNames):
    figTabs = go.Figure()

    for i in range(len(cityNames)):
        figTabs.add_trace(
            go.Scatter(x=df_core_component_city_time[df_core_component_city_time['Location'] == cityNames[i]]['Date'],
                       y=df_core_component_city_time[df_core_component_city_time['Location'] == cityNames[i]][
                           featureName],
                       mode='lines',
                       name=cityNames[i]))

    figTabs.update_layout(title=f'Line plot of {featureName} hue by city',
                          xaxis_title='Date')
    if featureName == 'MinTemp' or featureName == 'MaxTemp':
        figTabs.update_layout(yaxis_title='Temperature (degrees C)')
    elif featureName == 'Rainfall':
        figTabs.update_layout(yaxis_title='Rainfall (mm)')
    else:
        figTabs.update_layout(yaxis_title='Wind Gust Speed (km/h)')

    return figTabs
#######################################
# Range slider
# Drop down menu
# Radio items

rangeSlider_layout = html.Div([
    html.Div(html.P('Range slider + Drop down menu + Radio items', className='h2')),
    dcc.Dropdown(id='dropdown_core', options=showCityNameDropdownOptions, value=showCityName[0],
                 placeholder='Select the city that you want to see'),
    dcc.RadioItems(
        id='radioItems_core',
        options=showFeatureOptions,
        value=showFeature[0]
    ),
    dcc.Graph(id='rangeSlider_graph'),
    dcc.RangeSlider(id='rangeSlider_core', min=dateYear.min(), max=dateYear.max(), step=1,
                    marks={
                        int(i): str(i) for i in range(dateYear.min(), dateYear.max() + 1)
                    },
                    value=[dateYear.min(), dateYear.max()])
], className='core-component-section')

@app.callback(
    Output(component_id='rangeSlider_graph', component_property='figure'),
    [Input(component_id='rangeSlider_core', component_property='value'),
     Input(component_id='dropdown_core', component_property='value'),
     Input(component_id='radioItems_core', component_property='value')]
)
def display_rangeSlider(rangeSlider, cityName, featureName):
    df_core_component_city_rangeSlider = df_core_component_city[
        (df_core_component_city['Date'] >= str(rangeSlider[0])) & (
                df_core_component_city['Date'] <= str(rangeSlider[1] + 1))]
    df_core_component_city_rangeSlider = df_core_component_city_rangeSlider[
        df_core_component_city_rangeSlider['Location'] == cityName]

    fig = px.line(data_frame=df_core_component_city_rangeSlider, x='Date', y=featureName, color='Location',
                  title=f'Line plot of {featureName} from {rangeSlider[0]} to {rangeSlider[1]}')
    if featureName == 'MinTemp' or featureName == 'MaxTemp':
        fig.update_layout(xaxis_title='Date', yaxis_title='Temperature (degrees C)')
    elif featureName == 'Rainfall':
        fig.update_layout(xaxis_title='Date', yaxis_title='Rainfall (mm)')
    else:
        fig.update_layout(xaxis_title='Date', yaxis_title='Wind Gust Speed (km/h)')
    return fig

#######################################
# Button + DataPickerRange
datePickerRange_layout = html.Div([
    html.Div(html.P('DataPickerRange + Button', className='h2')),
    dbc.Row([
        dbc.Label("City", width=1),
        dbc.Col(
            dcc.Dropdown(id='cityName_dropDownMenu_core',
                         options=showCityNameDropdownOptions,
                         value=showCityName[0]),
        ),
    ], className="mb-3"),
    dbc.Row([
        dbc.Label("Date", width=1),
        dbc.Col(
            dcc.DatePickerRange(id='dataPickerRange_core',
                                min_date_allowed=minDate,
                                max_date_allowed=maxDate,
                                start_date=minDate,
                                end_date=maxDate,
                                display_format='Y-M-D',
                                start_date_placeholder_text='Y-M-D'
                                ),
        ),
    ], className="mb-3"),
    dbc.Row(
        [
            dbc.Col(
                dbc.Button("Submit", id='button_core', color="primary"), width="auto"
            ),
        ], className="mb-3"),
    dcc.Graph(id='dataPickerRange_graph'),

])

@app.callback(
    Output(component_id='dataPickerRange_graph', component_property='figure'),
    [Input(component_id='button_core', component_property='n_clicks')],
    [State(component_id='cityName_dropDownMenu_core', component_property='value'),
     State(component_id='dataPickerRange_core', component_property='start_date'),
     State(component_id='dataPickerRange_core', component_property='end_date')]
)
def display_dataPickerRange(clicks, cityName, start_date, end_date):
    # print(f'start_date: {start_date}, end_date: {end_date}')
    df_dataPickerRange = df_core_component_city[(df_core_component_city['Date'] >= start_date) & (
            df_core_component_city['Date'] <= end_date)]
    df_dataPickerRange = df_dataPickerRange[df_dataPickerRange['Location'] == cityName]
    fig = go.Figure()
    if clicks is not None:
        fig.add_trace(go.Scatter(x=df_dataPickerRange['Date'],
                                 y=df_dataPickerRange['MinTemp'],
                                 mode='lines', name='MinTemp')),
        fig.add_trace(go.Scatter(x=df_dataPickerRange['Date'],
                                 y=df_dataPickerRange['MaxTemp'],
                                 mode='lines', name='MaxTemp')),
        fig.update_layout(title=f'Highest and Lowest Temperatures in {cityName}',
                          xaxis_title='Date',
                          yaxis_title='Temperature (degrees C)')
    return fig
#######################################
# Input field + Output field + Text area

email_input = html.Div(
    [
        dbc.Input(id="input-email-core", type="email", value=""),
        dbc.FormText("We only accept gmail..."),
        dbc.FormFeedback("That looks like a gmail address :-)", type="valid"),
        dbc.FormFeedback(
            "Sorry, we only accept gmail for some reason...",
            type="invalid",
        ),
    ]
)

inputOutput_layout = html.Div([
    html.Div(html.P('Input field + Output field + Text area', className='h2')),
    html.Div([
        dbc.Form([
            dbc.Label("Email", width="auto"),
            email_input,
            dbc.Label("Password", width="auto"),
            dbc.Input(id='input-password-core', type="password", placeholder="Enter password"),
            dbc.Label("Textarea", width="auto"),
            dbc.Textarea(id='input-textarea-core'),
            dbc.Button("Submit", id='input-button-core', color="primary", style={'margin-top': '10px'}),
            html.Div(id='result-input')
        ])
    ])

])

@app.callback(
    [Output("input-email-core", "valid"), Output("input-email-core", "invalid")],
    [Input("input-email-core", "value")],
)
def check_validity(text):
    if text:
        is_gmail = text.endswith("@gmail.com")
        return is_gmail, not is_gmail
    return False, False

@app.callback(
    Output(component_id='result-input', component_property='children'),
    [Input(component_id='input-button-core', component_property='n_clicks')],
    [State(component_id='input-email-core', component_property='value'),
     State(component_id='input-password-core', component_property='value'),
     State(component_id='input-textarea-core', component_property='value')]
)
def show_input(clicks, email, password, textarea):
    if clicks is not None:
        return f'email : {email}, password : {password}, textarea : {textarea}'
    return f'results are empty'
#######################################
# upload + download
updownload_layout = html.Div([
    html.Div(html.P('Upload + Download component', className='h2')),
    html.Div(html.P('Upload csv', className='h6')),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
    html.Br(),
    html.Div(html.P('Download button', className='h6')),
    dbc.Button("Download dataset", id="btn-download-txt", color="secondary", className="me-1"),
    dcc.Download(id="download-core")
])

@app.callback(
    Output("download-core", "data"),
    Input("btn-download-txt", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, filename="weatherAUS.csv")

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
#######################################
# core_component main page
core_component = html.Div([
    html.Div(className='container', children=[
        dbc.Row(dbc.Col(html.P("Hello, Welcome to Core Component!", className='head-title', ))),
        dbc.Row(dbc.Col(tabs_layout)),
        dbc.Row(dbc.Col(rangeSlider_layout)),
        dbc.Row(dbc.Col(datePickerRange_layout)),
        dbc.Row(dbc.Col(inputOutput_layout)),
        dbc.Row(dbc.Col(updownload_layout)),
    ])
])
#######################################
# figure section
#######################################
# simplify dataset
df_figure = df_weather[
    ['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustDir', 'WindGustSpeed', 'RainToday',
     'RainTomorrow']].copy()
df_figure.dropna(how='any', inplace=True)
showFeature = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed']
showCityName = ['Albury', 'BadgerysCreek', 'Cobar']
df_figure_city_time = df_figure[
    (df_figure['Date'] > '2017-01-01') & (df_figure['Location'].isin(showCityName))]
df_figure_city = df_figure[df_figure['Location'].isin(showCityName)]

#######################################
# Line-plot
figLineplot = px.line(data_frame=df_figure_city_time, x='Date', y='MinTemp', color='Location',
                      title='Line plot of minimum temperature in degrees Celsius hue city')
figLineplot.update_layout(yaxis_title='MinTemp (℃)')

lineplot_layout = html.Div([
    html.P('Line-plot', className='h2'),
    dcc.Graph(figure=figLineplot)
], className='figure-section')
#######################################
# Bar-plot: stack, group
figBarplotStack = px.bar(data_frame=df_figure_city, x='Location', y='Rainfall', color='RainTomorrow',
                         title='Bar plot of today rainfall in different cities hue by rain tomorrow')
figBarplotGroup = px.bar(data_frame=df_figure_city, x='Location', y='RainToday', color='RainTomorrow', barmode='group',
                         title='Bar plot in different cities group by RainTomorrow')

figBarplotStack.update_layout(yaxis_title='Count of Rainfall')
figBarplotGroup.update_layout(yaxis_title='Count of Rainfall')
barplot_layout = html.Div([
    html.P('Bar-plot', className='h2'),
    dcc.Graph(figure=figBarplotStack),
    dcc.Graph(figure=figBarplotGroup),
], className='figure-section')
#######################################
# count-plot (There is only histogram in plotly)
figCount = px.histogram(data_frame=df_figure_city, x='RainToday', color='RainToday',
                        title='Count plot of Rain Today')

countplot_layout = html.Div([
    html.P('Count-plot(histogram)', className='h2'),
    dcc.Graph(figure=figCount)
], className='figure-section')
#######################################
# Cat-plot(scatter plot)
figCatplot = px.scatter(data_frame=df_figure_city_time, y='MaxTemp', x='Location', size='Rainfall',
                        color='Location',
                        title='Cat-plot of MaxTemp size by rainfall hue city')
figCatplot.update_layout(yaxis_title='MaxTemp (℃)')
catplot_layout = html.Div([
    html.P('Cat-plot(scatter plot)', className='h2'),
    dcc.Graph(figure=figCatplot)
], className='figure-section')
#######################################
# Pie-chart
labels = df_figure_city_time['WindGustDir'].value_counts().keys().tolist()
values = df_figure_city_time['WindGustDir'].value_counts().tolist()
figPirchart = go.Figure(go.Pie(values=values, labels=labels,
                               title='Pie chart of the wind gust direction'))

piechart_layout = html.Div([
    html.P('Pie-chart', className='h2'),
    dcc.Graph(figure=figPirchart)
], className='figure-section')
#######################################
# Displot
figDisplot = px.histogram(data_frame=df_figure_city_time, x='MaxTemp', color='Location',
                          title='Displot of MaxTemp hue by city')

displot_layout = html.Div([
    html.P('Displot', className='h2'),
    dcc.Graph(figure=figDisplot)
], className='figure-section')
#######################################
# Pair plot(scatter_matrix)
figPairplot = px.scatter_matrix(data_frame=df_figure_city_time, dimensions=showFeature,
                                color='Location',
                                title='Pair plot about MinTemp, MaxTemp, Rainfall, WindGustSpeed hue by city')

pairplot_layout = html.Div([
    html.P('Pair plot(scatter_matrix)', className='h2'),
    dcc.Graph(figure=figPairplot)
], className='figure-section')
#######################################
# Heatmap
df_showCity_heatmap = df_figure_city.copy()
df_showCity_heatmap = df_showCity_heatmap[['Date', 'MaxTemp']]
df_showCity_heatmap_new = df_showCity_heatmap.groupby(pd.PeriodIndex(df_showCity_heatmap['Date'], freq="M"))[
    'MaxTemp'].mean()
df_showCity_heatmap_new = pd.DataFrame(df_showCity_heatmap_new)
df_showCity_heatmap_new['Date'] = df_showCity_heatmap_new.index
df_showCity_heatmap_new['year'] = df_showCity_heatmap_new['Date'].dt.year
df_showCity_heatmap_new['month'] = df_showCity_heatmap_new['Date'].dt.month
df_showCity_heatmap_new = df_showCity_heatmap_new.pivot('year', 'month', 'MaxTemp')

figHeatmap = px.imshow(df_showCity_heatmap_new, text_auto=True, aspect="auto",
                       title='Heatmap of MaxTemp average in month and year')

heatmap_layout = html.Div([
    html.P('Heatmap', className='h2'),
    dcc.Graph(figure=figHeatmap)
], className='figure-section')
#######################################
# Hist-plot
hist_data = [df_figure_city_time['MinTemp'].tolist(), df_figure_city_time['MaxTemp'].tolist()]
group_labels = ['MinTemp', 'MaxTemp']
figHistplot = ff.create_distplot(hist_data, group_labels)
figHistplot.update_layout(title_text='Hist-plot of MaxTemp and MinTemp',
                          xaxis_title='Celsius degree(℃)',
                          yaxis_title='percent')

histplot_layout = html.Div([
    html.P('Hist-plot', className='h2'),
    dcc.Graph(figure=figHistplot)
], className='figure-section')
#######################################
# QQ-plot
from statsmodels.graphics.gofplots import qqplot

qqplot_data = qqplot(data=df_figure_city_time['MinTemp'], line='s').gca().lines

figQQplot = go.Figure()

figQQplot.add_trace({
    'type': 'scatter',
    'x': qqplot_data[0].get_xdata(),
    'y': qqplot_data[0].get_ydata(),
    'mode': 'markers',
    'marker': {
        'color': '#19d3f3'
    }
})

figQQplot.add_trace({
    'type': 'scatter',
    'x': qqplot_data[1].get_xdata(),
    'y': qqplot_data[1].get_ydata(),
    'mode': 'lines',
    'line': {
        'color': '#636efa'
    }

})

figQQplot['layout'].update({
    'title': 'Quantile-Quantile Plot of MinTemp',
    'xaxis': {
        'title': 'Theoritical Quantities',
        'zeroline': False
    },
    'yaxis': {
        'title': 'Sample Quantities'
    },
    'showlegend': False,
    'width': 800,
    'height': 700,
})

qqplot_layout = html.Div([
    html.P('QQ-plot', className='h2'),
    dcc.Graph(figure=figQQplot)
], className='figure-section')
#######################################
# Kernal density estimate
figKde = px.density_contour(df_figure_city_time, x="MinTemp", y="WindGustSpeed", color="Location",
                            title='Kde plot of WindGustSpeed versus MinTemp hue by city')
figKde.update_layout(yaxis_title='WindGustSpeed (km/h)',
                     xaxis_title='MinTemp (℃)')
kde_layout = html.Div([
    html.P('Kernal density estimate', className='h2'),
    dcc.Graph(figure=figKde)
], className='figure-section')
#######################################
# Scatter plot and regression line
figScatterplot = px.scatter(data_frame=df_figure_city_time, y='WindGustSpeed', x='MinTemp',
                            trendline="ols",
                            title='Scatter plot of WindGustSpeed versus MinTemp and regression line')
figScatterplot.update_layout(yaxis_title='WindGustSpeed (km/h)',
                             xaxis_title='MinTemp (℃)')
scatterplot_layout = html.Div([
    html.P('Scatter plot and regression line', className='h2'),
    dcc.Graph(figure=figScatterplot)
], className='figure-section')
#######################################
# Multivariate Box plot
figBoxplot = px.box(data_frame=df_figure_city_time, x='Location', y='MinTemp', color='Location',
                    title="Box plot of MinTemp in different cities")
figBoxplot.update_layout(yaxis_title='MinTemp (℃)')
boxplot_layout = html.Div([
    html.P('Multivariate Box plot', className='h2'),
    dcc.Graph(figure=figBoxplot)
], className='figure-section')
#######################################
# Area plot
figAreaplot = px.area(df_figure_city_time, x="Date", y="Rainfall", color="Location", line_group="Location",
                      title='Area plot of Rainfall hue by city')
figAreaplot.update_layout(yaxis_title='Rainfall (mm)')
areplot_layout = html.Div([
    html.P('Area plot', className='h2'),
    dcc.Graph(figure=figAreaplot)
], className='figure-section')
#######################################
# Violin plot
figViolin = px.violin(df_figure_city_time, y="MaxTemp", x="Location", color="Location",
                      box=True, points="all", title='Violin plot of MaxTemp hue by city')
figViolin.update_layout(yaxis_title='MaxTemp (℃)')
violinplot_layout = html.Div([
    html.P('Violin plot', className='h2'),
    dcc.Graph(figure=figViolin)
], className='figure-section')

#######################################
# figure_section main page
figure_section = html.Div([
    html.Div(className='container', children=[
        dbc.Row(dbc.Col(html.P("Hello, Welcome to Figure section!", className='head-title', ))),
        lineplot_layout,
        barplot_layout,
        countplot_layout,
        catplot_layout,
        piechart_layout,
        displot_layout,
        pairplot_layout,
        heatmap_layout,
        histplot_layout,
        qqplot_layout,
        kde_layout,
        scatterplot_layout,
        boxplot_layout,
        areplot_layout,
        violinplot_layout
    ])
])
#######################################
# city-compare
#######################################

#######################################
city_input_comapre = dbc.Row(
    [
        dbc.Label("City", width=1),
        dbc.Col(
            dcc.Dropdown(id='cityName_dropDownMenu_compare',
                         options=cityNameDropdownOptions, multi=True),
        ),
    ],
    className="mb-3",
)

date_input_compare = dbc.Row(
    [
        dbc.Label("Date", width=1),
        dbc.Col(
            dcc.DatePickerRange(id='date_comapre',
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

submit_compare = dbc.Row(
    [
        dbc.Col(
            dbc.Button("Submit", id='submit_compare', color="primary"), width="auto"
        ),
    ],
    className="mb-3",
)

select_layout = html.Div([
    city_input_comapre,
    date_input_compare,
    submit_compare,
    html.Div(id='city_compare_figure'),
])

@app.callback(
    Output(component_id='city_compare_figure', component_property='children'),
    [Input(component_id='submit_compare', component_property='n_clicks')],
    [State(component_id='cityName_dropDownMenu_compare', component_property='value'),
     State(component_id='date_comapre', component_property='start_date'),
     State(component_id='date_comapre', component_property='end_date')]
)
def display_city_Compare(clicks, cityNameList, start_date, end_date):
    figMinTemp = go.Figure()
    figMaxTemp = go.Figure()
    figWindGustSpeed = go.Figure()
    figTempViolin = go.Figure()
    figRainfall = go.Figure()
    figBoxplot = go.Figure()
    figCatplot = go.Figure()
    figAreaplot = go.Figure()
    figHeatmap = go.Figure()

    if clicks is not None:
        # create new dafaframe fit condition
        df_display_city_compare = df_weather[(df_weather['Date'] >= start_date) & (df_weather['Date'] <= end_date)]
        df_display_city_compare = df_display_city_compare[df_display_city_compare['Location'].isin(cityNameList)]
        df_display_city_compare['Rainfall'].fillna(0, inplace=True)
        for i in range(len(cityNameList)):
            df_temp = df_display_city_compare[df_display_city_compare['Location'] == cityNameList[i]]
            figMinTemp.add_trace(go.Scatter(
                x=df_temp['Date'],
                y=df_temp['MinTemp'],
                mode='lines',
                name=f'MinTemp of {cityNameList[i]}'))

            figMaxTemp.add_trace(go.Scatter(
                x=df_temp['Date'],
                y=df_temp['MaxTemp'],
                mode='lines',
                name=f'MaxTemp of {cityNameList[i]}'))

            figWindGustSpeed.add_trace(go.Scatter(
                x=df_temp['Date'],
                y=df_temp['WindGustSpeed'],
                mode='lines',
                name=f'WindGustSpeed of {cityNameList[i]}'))

            figRainfall.add_trace(go.Scatter(
                x=df_temp['Date'],
                y=df_temp['Rainfall'],
                mode='lines',
                name=f'Rainfall of {cityNameList[i]}'))

            figTempViolin.add_trace(go.Violin(
                x=df_temp['Location'],
                y=df_temp['MaxTemp'],
                legendgroup=f'MaxTemp of {cityNameList[i]}', scalegroup=f'MaxTemp of {cityNameList[i]}',
                name=f'MaxTemp of {cityNameList[i]}',
                side='negative',
                line_color='lightseagreen',
            ))

            figTempViolin.add_trace(go.Violin(
                x=df_temp['Location'],
                y=df_temp['MinTemp'],
                legendgroup=f'MinTemp of {cityNameList[i]}', scalegroup=f'MinTemp of {cityNameList[i]}',
                name=f'MinTemp of {cityNameList[i]}',
                side='positive',
                line_color='mediumpurple',
            ))

        figMinTemp.update_layout(title=f'MinTemp of selected city',
                                 yaxis_title='MinTemp(℃)',
                                 xaxis_title='Date')
        figMaxTemp.update_layout(title=f'MaxTemp of selected city',
                                 yaxis_title='MaxTemp(℃)',
                                 xaxis_title='Date')
        figWindGustSpeed.update_layout(title=f'WindGustSpeed of selected city',
                                       yaxis_title='WindGustSpeed(km/h)',
                                       xaxis_title='Date')
        figRainfall.update_layout(title=f'Rainfall of selected city',
                                  yaxis_title='Rainfall(mm)',
                                  xaxis_title='Date')
        figTempViolin.update_layout(title=f'Violin of MinTemp and MaxTemp',
                                    yaxis_title='Celsius(℃)',
                                    xaxis_title='Date')
        figTempViolin.update_traces(meanline_visible=True,
                                    points='all',  # show all points
                                    jitter=0.05,  # add some jitter on points for better visibility
                                    scalemode='count')  # scale violin plot area with total count
        # Multivariate Box plot
        figBoxplot = px.box(data_frame=df_display_city_compare, x='Location', y='MinTemp', color='Location',
                            title="Box plot of MinTemp in different cities")
        figBoxplot.update_layout(yaxis_title='MinTemp (℃)')
        # Cat-plot(scatter plot)
        figCatplot = px.scatter(data_frame=df_display_city_compare, y='MaxTemp', x='Location', size='Rainfall',
                                color='Location',
                                title='Cat-plot of MaxTemp size by rainfall hue city')
        figCatplot.update_layout(yaxis_title='MaxTemp (℃)')
        # Area plot
        figAreaplot = px.area(df_display_city_compare, x="Date", y="Rainfall", color="Location", line_group="Location",
                              title='Area plot of Rainfall hue by city')
        figAreaplot.update_layout(yaxis_title='Rainfall (mm)')
        # Heatmap
        df_showCity_heatmap = df_display_city_compare.copy()
        df_showCity_heatmap = df_showCity_heatmap[['Date', 'MaxTemp']]
        df_showCity_heatmap_new = df_showCity_heatmap.groupby(pd.PeriodIndex(df_showCity_heatmap['Date'], freq="M"))[
            'MaxTemp'].mean()
        df_showCity_heatmap_new = pd.DataFrame(df_showCity_heatmap_new)
        df_showCity_heatmap_new['Date'] = df_showCity_heatmap_new.index
        df_showCity_heatmap_new['year'] = df_showCity_heatmap_new['Date'].dt.year
        df_showCity_heatmap_new['month'] = df_showCity_heatmap_new['Date'].dt.month
        df_showCity_heatmap_new = df_showCity_heatmap_new.pivot('year', 'month', 'MaxTemp')
        figHeatmap = px.imshow(df_showCity_heatmap_new, text_auto=True, aspect="auto",
                               title='Heatmap of MaxTemp average in month and year')



    city_compare_layout = html.Div([
        html.Div(html.P('Line - plot of MinTemp', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figMinTemp))),
        html.Div(html.P('Line - plot of MaxTemp', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figMaxTemp))),
        html.Div(html.P('Line - plot of WindGustSpeed', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figWindGustSpeed))),
        html.Div(html.P('Violin - plot of MaxTemp and MinTemp', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figTempViolin))),
        html.Div(html.P('Line - plot of Rainfall', className='h2')),
        dbc.Row(dbc.Col(dcc.Graph(figure=figRainfall))),
        html.Div(html.P('Multivariate Box plot', className='h2')),
        dcc.Graph(figure=figBoxplot),
        html.Div(html.P('Cat-plot(scatter plot)', className='h2')),
        dcc.Graph(figure=figCatplot),
        html.Div(html.P('Area plot', className='h2')),
        dcc.Graph(figure=figAreaplot),
        html.Div(html.P('Heatmap plot', className='h2')),
        dcc.Graph(figure=figHeatmap)
    ])

    return city_compare_layout
#######################################


#######################################
# city-compare main page
city_compare = html.Div([
    html.Div(className='container', children=[
        dbc.Row(dbc.Col(html.P("Hello, Welcome to City Compare!", className='head-title'))),
        select_layout,

    ])
])
#######################################
# index-page
#######################################
nav = dbc.Nav(
    [
        dcc.Location(id='url', refresh=False),
        dbc.NavItem(dbc.NavLink("City", id='city-page', active=True, href="/city-page")),
        dbc.NavItem(dbc.NavLink("Core Components", id='core-component', active=True, href="/core-component")),
        dbc.NavItem(dbc.NavLink("Figure Section", id='figure-section', active=True, href="/figure-section")),
        dbc.NavItem(dbc.NavLink("City Compare", id='city-compare', active=True, href="/city-compare")),
    ]
)

@app.callback(
    Output(component_id='page-main-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def navLink(pathname):
    if pathname == '/city-page':
        return city_page
    elif pathname == '/core-component':
        return core_component
    elif pathname == '/figure-section':
        return figure_section
    elif pathname == '/city-compare':
        return city_compare
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
                    [],
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
                html.Div('Rain in Australia', className='head-title'),
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

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
