import numpy as np
import plotly.express as px
import dash as dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

my_app = dash.Dash('My app', external_stylesheets=external_stylesheets)

my_app.layout = html.Div([
    dcc.Graph(id='my-graph'),
    html.P('Mean'),
    dcc.Slider(id='mean', min=-3, max=3, value=0,
               marks={-3: "-3", -2: "-2", -1: "-1", 0: "0", 1: '1', 2: '2', 3: '3'}),

    html.Br(),
    html.P('std'),
    dcc.Slider(id='std', min=1, max=3, value=1,
               marks={1: '1', 2: '2', 3: '3'}),

    html.Br(),
    html.P('Number of the samples'),
    dcc.Slider(id='size', min=1, max=10000, value=100,
               marks={100:'100',500:'500',1000:'1000',5000:'5000'}),

    html.Br(),
    html.P('Number of the bins'),
    dcc.Dropdown(id='bins',
                 options=[
                     {'label': 20, 'value': 20},
                     {'label': 30, 'value': 30},
                     {'label': 40, 'value': 40},
                     {'label': 60, 'value': 60},
                     {'label': 80, 'value': 80},
                     {'label': 100, 'value': 100},
                 ],
                 value=20, clearable=False),
])


@my_app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='mean', component_property='value'),
     Input(component_id='std', component_property='value'),
     Input(component_id='size', component_property='value'),
     Input(component_id='bins', component_property='value')]
)
def deplay_color(mean, std, size, bins):
    x = np.random.normal(mean, std, size=size)
    fig = px.histogram(x = x, nbins = bins, range_x=[-5,5])
    return fig


# my_app.server.run(debug=True)
my_app.run_server(
    debug=True,
    port=8036,
)
