import dash as dash
from dash import dcc
from dash import html

my_app = dash.Dash('My app')
my_app.layout = html.Div([
    html.H1('Homework 1'),
    html.Button('Submit', id='HW1', n_clicks=0),

    html.H1('Homework 2'),
    html.Button('Submit', id='HW2', n_clicks=0),

    html.H1('Homework 3'),
    html.Button('Submit', id='HW3', n_clicks=0),

    html.H1('Homework 4'),
    html.Button('Submit', id='HW4', n_clicks=0),
])

# my_app.server.run(debug=True)
my_app.run_server(
    port=8033,
    host='0.0.0.0'
)