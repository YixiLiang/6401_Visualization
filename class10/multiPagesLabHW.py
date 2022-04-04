import numpy as np
import plotly.express as px
import dash as dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import math
from scipy.fft import fft

# website
# https://dashapp-sobkbafqpq-wn.a.run.app/

#######################################
# Index page
#######################################
# external_stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
tabs_styles = {
    'height': '44px'
}

tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

my_app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
my_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Lab5', href='/page-1'),
    html.Br(),
    dcc.Link('HW4', href='/page-2'),
])

# Update the index
@my_app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return lab5_layout
    elif pathname == '/page-2':
        return hw4_layout
    else:
        return index_page



lab5_layout = html.Div([
    dcc.Link('Back to Index', href='/'),
    dcc.Tabs(id="tabs-inline", value='tab-1', children=[
        dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 3', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 4', value='tab-4', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 5', value='tab-5', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Tab 6', value='tab-6', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline-3')
])

@my_app.callback(Output('tabs-content-inline-3', 'children'),
              Input('tabs-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return covid_layout
    elif tab == 'tab-2':
        return quadratic_function_layout
    elif tab == 'tab-3':
        return calculator
    elif tab == 'tab-4':
        return normal_Distribution_layout
    elif tab == 'tab-5':
        return polynomial_layout
    elif tab == 'tab-6':
        return bar_layout

#######################################
# Q1
#######################################
# load data
df1 = pd.read_csv('https://raw.githubusercontent.com/rjafari979/Complex-Data-Visualization-/main/CONVENIENT_global_confirmed_cases.csv')
df1 = df1.dropna(axis=0, how="any")
# China_sum
df1['China_sum'] = df1.iloc[0:, 57:90].astype(float).sum(axis=1)
# United Kingdom_sum
df1['United Kingdom_sum'] = df1.iloc[0:, 249:260].astype(float).sum(axis=1)
# 7 countries
df_covid = df1.copy()
countryName = ['US', 'Brazil', 'United Kingdom_sum', 'China_sum', 'India', 'Italy', 'Germany']
# df.rename(columns={"Country/Region": "Date"}, inplace=True)
df_covid['date'] = pd.date_range(start='1-23-20', end='11-22-20')

# fill dropDown
optionsCountriesList = []
for i in range(len(countryName)):
    dic = {'label': countryName[i], 'value': countryName[i]}
    optionsCountriesList.append(dic)

covid_layout = html.Div([
    html.H3('COVID global confirmed cases'),
    dcc.Graph(id='covid-graph'),
    html.H6('Pick the country Name'),
    dcc.Dropdown(
        id='country-drop',
        options=optionsCountriesList,
        value=countryName[0],
        clearable=False
    ),
    html.Br(),
])

@my_app.callback(
    Output(component_id='covid-graph', component_property='figure'),
    [Input(component_id='country-drop', component_property='value')]
)
def countryDisplay(country):
    fig = px.line(df_covid, x='date', y=[country])
    return fig

#######################################
# Q2
#######################################
quadratic_function_layout = html.Div([
    html.H3('Quadratic function 𝑓(𝑥)=𝑎𝑥2+𝑏𝑥+𝑐'),
    dcc.Graph(id='quadratic-function'),
    html.P('a value'),
    dcc.Slider(
        id='slider-a',
        min=-100,
        max=100,
        value=0),

    html.Br(),
    html.P('b value'),
    dcc.Slider(
        id='slider-b',
        min=-100,
        max=100,
        value=0),

    html.Br(),
    html.P('c value'),
    dcc.Slider(
        id='slider-c',
        min=-100,
        max=100,
        value=0),
])

@my_app.callback(
    Output(component_id='quadratic-function', component_property='figure'),
    [Input(component_id='slider-a', component_property='value'),
     Input(component_id='slider-b', component_property='value'),
     Input(component_id='slider-c', component_property='value')]
)
def quadratic_function(a, b, c):
    # create 1000 samples from -2 to 2 which have same step
    x = np.linspace(-2, 2, 1000)
    y = a * x ** 2 + b * x + c
    fig = px.line(x=x, y=y)
    return fig


#######################################
# Q3 calculator
#######################################
calculator = html.Div([
    html.H3('Calculator', style={'text-align': 'center'}),
    html.H6('Please enter the first number'),
    html.H6('Input: ', style={'display': 'inline-block', 'margin-right': 20}),
    dcc.Input(id='firstNumber', type='number', style={'display': 'inline-block'}),
    html.Br(),
    html.Br(),
    dcc.Dropdown(
        id='calculator-operator',
        options=[
            {'label': '+', 'value': 'Addition'},
            {'label': '-', 'value': 'Subtraction'},
            {'label': '*', 'value': 'Multiplication'},
            {'label': '/', 'value': 'Division'},
            {'label': 'log', 'value': 'Log'},
            {'label': '^', 'value': 'Square'},
            {'label': '√¯', 'value': 'Root Square'},
        ],
    ),
    html.Br(),
    html.H6('Please enter the second number'),
    html.H6('Input: ', style={'display': 'inline-block', 'margin-right': 20}),
    dcc.Input(id='secondNumber', type='number', style={'display': 'inline-block'}),
    html.Br(),
    html.Div(id='calculator-out')
])


@my_app.callback(
    Output(component_id='calculator-out', component_property='children'),
    [Input(component_id='firstNumber', component_property='value'),
     Input(component_id='secondNumber', component_property='value'),
     Input(component_id='calculator-operator', component_property='value')]
)
def calculate(firstNumber, secondNumber, calculatorOperator):
    if firstNumber and secondNumber and calculatorOperator is not None:
        if calculatorOperator == 'Addition':
            result = firstNumber + secondNumber
        elif calculatorOperator == 'Subtraction':
            result = firstNumber - secondNumber
        elif calculatorOperator == 'Multiplication':
            result = firstNumber * secondNumber
        elif calculatorOperator == 'Division':
            result = firstNumber / secondNumber
        elif calculatorOperator == 'Log':
            result = f'that the log of first number is {math.log(firstNumber)},and the log of second number is {math.log(secondNumber)}'
        elif calculatorOperator == 'Square':
            result = f'that the square of first number is {firstNumber ** 2}, and the square of second number is {secondNumber ** 2}'
        elif calculatorOperator == 'Root Square':
            result = f'that the root square of first number is {math.sqrt(firstNumber)},and the root square of second number is {math.sqrt(secondNumber)}'
        return html.H6(f'The Output value is {result}')
    else:
        return html.H6('The result will only display when all the inputs are not None, and the function is valid', style={'color': 'red'})


#######################################
# Q4 standard
#######################################

normal_Distribution_layout = html.Div([
    html.H3('Gaussian distribution'),
    dcc.Graph(id='normal_distribution_graph'),
    html.P('Mean'),
    dcc.Slider(id='mean', min=-2, max=2, step=1, value=0,
               marks={-2: "-2", -1: "-1", 0: "0", 1: '1', 2: '2'}),

    html.Br(),
    html.P('Std'),
    dcc.Slider(id='std', min=1, max=3, step=1, value=1,
               marks={1: '1', 2: '2', 3: '3'}),

    html.Br(),
    html.P('Number of the samples'),
    dcc.Slider(id='size', min=100, max=10000, step=500, value=100),

    html.Br(),
    html.P('Number of the bins'),
    dcc.Slider(id='bins', min=20, max=100, step=10, value=20),

])


@my_app.callback(
    Output(component_id='normal_distribution_graph', component_property='figure'),
    [Input(component_id='mean', component_property='value'),
     Input(component_id='std', component_property='value'),
     Input(component_id='size', component_property='value'),
     Input(component_id='bins', component_property='value')]
)
def normal_distribution(mean, std, size, bins):
    x = np.random.normal(mean, std, size)
    fig = px.histogram(x=x, nbins=bins, range_x=[-2, 2])
    return fig


#######################################
# Q5 polynomial
#######################################
polynomial_layout = html.Div([
    html.H3('Polynomial function'),
    html.H6('Please enter the polynomial order'),
    dcc.Input(id='polynomial', type='number', value=0, placeholder="default number is 0"),
    dcc.Graph(id='poly-graph')
])


@my_app.callback(
    Output(component_id='poly-graph', component_property='figure'),
    [Input(component_id='polynomial', component_property='value')]
)
def polynomial(polynomial):
    x = np.linspace(-2, 2, 1000)
    if polynomial is None:
        y = np.power(x, 0)
    else:
        y = np.power(x, polynomial)
    fig = px.line(x=x, y=y)
    return fig

#######################################
# Q6 group bar plot
#######################################
df_bar = pd.DataFrame(
    {"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"], "Amount": [4, 1, 2, 2, 4, 5],
     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]})

fig = px.bar(df_bar, x='Fruit', y='Amount', color='City', barmode='group')

bar_layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Hello Dash1'),
            dcc.Graph(id='fruit-graph1', figure=fig),
            html.H5('Slider1'),
            dcc.Slider(id='fruit-slider1', min=0, max=20, step=1, value=10)
        ], className="six columns"),
        html.Div([
            html.H1('Hello Dash2'),
            dcc.Graph(id='fruit-graph2', figure=fig),
            html.H5('Slider2'),
            dcc.Slider(id='fruit-slider2', min=0, max=20, step=1, value=10)
        ], className="six columns")
    ], className='row'),
    html.Br(),
    html.Div([
        html.Div([
            html.H1('Hello Dash3'),
            dcc.Graph(id='fruit-graph3', figure=fig),
            html.H5('Slider3'),
            dcc.Slider(id='fruit-slider3', min=0, max=20, step=1, value=10)
        ], className="six columns"),
        html.Div([
            html.H1('Hello Dash4'),
            dcc.Graph(id='fruit-graph4', figure=fig),
            html.H5('Slider4'),
            dcc.Slider(id='fruit-slider4', min=0, max=20, step=1, value=10)
        ], className="six columns")
    ], className='row')
])



###############################################################################################

#######################################
# Index page
#######################################

hw4_layout = html.Div([
    dcc.Link('Back to Index', href='/'),
    html.H1('Homework 4', style={'textAlign': 'center'}),
    html.Br(),
    dcc.Tabs(id='hw-questions', children=[
        dcc.Tab(label='Question1', value='q1'),
        dcc.Tab(label='Question2', value='q2'),
        dcc.Tab(label='Question3', value='q3')], value='q1'),
    html.Div(id='layout')
])


@my_app.callback(
    Output(component_id='layout', component_property='children'),
    [Input(component_id='hw-questions', component_property='value')]
)
def update_layout(ques):
    if ques == 'q1':
        return question1_layout
    elif ques == 'q2':
        return question2_layout
    elif ques == 'q3':
        return question3_layout


#######################################
# Q1 displays the entered data
#######################################
question1_layout = html.Div([
    html.B('Change the value in the textbox to see callbacks in action'),
    html.Br(),
    html.P('Input:', style={'display': 'inline-block', 'margin-right': 20}),
    dcc.Input(id='input1', type='text'),
    html.Div(id='output_Input_text')
])


@my_app.callback(
    Output(component_id='output_Input_text', component_property='children'),
    [Input(component_id='input1', component_property='value')]
)
def display_input(input):
    return f'The output value is {input}'


#######################################
# Q2 f(x) = sin(x) + noise / Fast Fourier Transform (FFT)
#######################################
question2_layout = html.Div([
    html.H6('Please enter the number of sinusoidal cycle', style={'font-weight': 'bold'}),
    dcc.Input(id='sinCycle', type='number', placeholder='The default number is 1', value=1),
    html.Br(),
    html.H6('Please enter the mean of the white noise', style={'font-weight': 'bold'}),
    dcc.Input(id='noiseMean', type='number', placeholder='The default number is 1', value=1),
    html.Br(),
    html.H6('Please enter the standard deviation of white noise', style={'font-weight': 'bold'}),
    dcc.Input(id='noiseStd', type='number', placeholder='The default number is 1', value=1),
    html.Br(),
    html.H6('Please enter the number of sample', style={'font-weight': 'bold'}),
    dcc.Input(id='sample', type='number', placeholder='The default number is 1000', value=1000),
    html.Br(),
    html.Br(),
    dcc.Graph(id='sin-graph'),
    html.Br(),
    html.H6('The fast fourier transform of above generated data', style={'font-weight': 'bold'}),
    dcc.Graph(id='fft-graph'),
])


@my_app.callback(
    [Output(component_id='sin-graph', component_property='figure'),
     Output(component_id='fft-graph', component_property='figure')],
    [Input(component_id='sinCycle', component_property='value'),
     Input(component_id='noiseMean', component_property='value'),
     Input(component_id='noiseStd', component_property='value'),
     Input(component_id='sample', component_property='value')]
)
def display_sinGraph(sinCycle, noiseMean, noiseStd, sample):
    if sinCycle is None:
        sinCycle = 1
    if sample is None:
        sample = 1000
    if noiseMean is None:
        noiseMean = 1
    if noiseStd is None:
        noiseStd = 1

    noise = np.random.normal(noiseMean, noiseStd, size=sample)

    x = np.linspace(-math.pi, math.pi, sample)

    y = [[math.sin(sinCycle * i) for i in x][k] + [noise[j] for j in range(sample)][k] for k in range(sample)]

    figSinCycle = px.line(x=x, y=y, range_x=[-math.pi, math.pi])
    N = sample
    T = 2 * math.pi / sample
    yf = list(fft(y))
    # xf = fftfreq(N, T)[:N // 2]
    figFft = px.line(x=x, y=np.abs(yf), range_x=[-math.pi, math.pi])
    return figSinCycle, figFft

#######################################
# Q3 drop-down menu
#######################################
question3_layout = html.Div([
    html.H3('Complex Data Visualization'),
    dcc.Dropdown(id='dropdown', options=[
        {'label': 'Introduction', 'value': 'Introduction'},
        {'label': 'Panda package', 'value': 'Panda package'},
        {'label': 'Seaborn package', 'value': 'Seaborn package'},
        {'label': 'Matplotlib Package', 'value': 'Matplotlib Package'},
        {'label': 'Principal Component Analysis', 'value': 'Principal Component Analysis'},
        {'label': 'Outlier Detection', 'value': 'Outlier Detection'},
        {'label': 'Interactive Visualization', 'value': 'Interactive Visualization'},
        {'label': 'Web-based App using Dash', 'value': 'Web-based App using Dash'},
        {'label': 'Tableau', 'value': 'Tableau'},
    ]),
    html.Div(id='output_Input_text2')
])


@my_app.callback(
    Output(component_id='output_Input_text2', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def display_dropdown(dropdown):
    return f'The selected item inside the dropdown menu is {dropdown}'


# my_app.server.run(debug=True)
my_app.run_server(
    debug=True,
    port=8036,
)