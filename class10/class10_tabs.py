import dash as dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

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
    html.H1('Question1'),
    html.H5('Test'),
    html.P('Input:'),
    dcc.Input(id='input1', type='text'),
    html.Div(id='output_Input')
])


@my_app.callback(
    Output(component_id='output_Input', component_property='children'),
    [Input(component_id='input1', component_property='value')]
)
def input1(input1):
    return f'The callback is {input1}'


question2_layout = html.Div([
    html.H1('Complex Data Visualization'),
    dcc.Dropdown(id='drop3', options=[
        {'label': 'Introduction', 'value': 'Introduction'},
        {'label': 'Panda Package', 'value': 'Panda Package'},
    ], value='Introduction'),
    html.Br(),
    html.Div(id='output3')
])

question3_layout = html.Div([
    html.H1('Time series analysis'),
    dcc.Checklist(id='my-check_list', options=[
        {'label': 'ACF', 'value': 'ACF'},
        {'label': 'GPAC', 'value': 'GPAC'},
        {'label': 'Correlation', 'value': 'Correlation'}
    ]),
    html.Br(),
    html.Div(id='output4')
])

my_app.run_server(
    port=8039,
    debug=True
)
