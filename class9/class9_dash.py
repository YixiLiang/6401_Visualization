import dash as dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

my_app = dash.Dash('My app')
my_app.layout = html.Div([
    html.H1('Homework 1'),
    html.Button('Submit', id='HW1', n_clicks=0),
    html.Div(id='countClick'),

    html.H1('Homework 2'),
    html.Button('Submit', id='HW2', n_clicks=0),

    html.H1('Homework 3'),
    html.Button('Submit', id='HW3', n_clicks=0),

    html.H1('Homework 4'),
    html.Button('Submit', id='HW4', n_clicks=0),
])

@my_app.callback(
    Output(component_id='countClick', component_property='children'),
    [Input(component_id='HW1', component_property='n_clicks')]
)

def countClick(click):
    return f'The click number is {click}'

# my_app.server.run(debug=True)
my_app.run_server(
    port=8033,
    debug=True
)