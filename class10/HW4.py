import math

import dash as dash
import pandas as pd
import numpy as np
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from scipy.fft import fft, fftfreq

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
my_app = dash.Dash('HW4', suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)

my_app.layout = html.Div([
    html.H1('Homework 4', style={'textAlign': 'center'}),
    html.Br(),
    dcc.Tabs(id='hw-questions', children=[
        dcc.Tab(label='Question1', value='q1'),
        dcc.Tab(label='Question2', value='q2'),
        dcc.Tab(label='Question3', value='q3')
    ]),
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


question2_layout = html.Div([
    html.H6('Please enter the number of sinusoidal cycle', style={'font-weight': 'bold'}),
    dcc.Input(id='sinCycle', type='number'),
    html.Br(),
    html.H6('Please enter the mean of the white noise', style={'font-weight': 'bold'}),
    dcc.Input(id='noiseMean', type='number'),
    html.Br(),
    html.H6('Please enter the standard deviation of white noise', style={'font-weight': 'bold'}),
    dcc.Input(id='noiseStd', type='number'),
    html.Br(),
    html.H6('Please enter the number of sample', style={'font-weight': 'bold'}),
    dcc.Input(id='sample', type='number'),
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
    T = 2*math.pi/sample
    yf = list(fft(y))
    # xf = fftfreq(N, T)[:N // 2]
    figFft = px.line(x=x, y=np.abs(yf), range_x=[-math.pi, math.pi])
    return figSinCycle,figFft


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


my_app.run_server(
    port=8039,
    debug=True
)
