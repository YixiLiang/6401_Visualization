import dash
from dash.dependencies import Input, Output, State
from dash import html
from dash import dcc

app = dash.Dash()

app.layout = html.Div([
    html.Button('Click Me', id='button'),
    html.H3(id='button-clicks'),

    html.Hr(),

    html.Label('Input 1'),
    dcc.Input(id='input-1'),

    html.Label('Input 2'),
    dcc.Input(id='input-2'),

    html.Label('Slider 1'),
    dcc.Slider(id='slider-1'),

    html.Button(id='button-2', n_clicks=0),

    html.Div(id='output')
])

@app.callback(
    Output('button-clicks', 'children'),
    [Input(component_id='button', component_property='n_clicks')])
def clicks(n_clicks):
    return 'Button has been clicked {} times'.format(n_clicks)

@app.callback(
    Output('output', 'children'),
    [Input(component_id='button-2', component_property='n_clicks')]
)
def compute(n_clicks):
    return f'A computation based off of {n_clicks}'

app.run_server(
    port=8040,
    debug=True
)