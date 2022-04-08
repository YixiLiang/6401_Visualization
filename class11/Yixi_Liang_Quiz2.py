import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output

tips = px.data.tips()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

my_app = dash.Dash('quiz2', external_stylesheets=external_stylesheets)

my_app.layout = html.Div([
    html.H6('Please select the feature from the menu'),
    dcc.Dropdown(
        id='drop-feature',
        options=[
            {'label': 'day', 'value': 'day'},
            {'label': 'time', 'value': 'time'},
            {'label': 'sex', 'value': 'sex'},
        ],
        value='day', clearable=False
    ),
    html.H6('Please select the output variable to be plotted'),
    dcc.Dropdown(
        id='drop-output',
        options=[
            {'label': 'total_bill', 'value': 'total_bill'},
            {'label': 'tip', 'value': 'tip'},
            {'label': 'size', 'value': 'size'},
        ],
        value='total_bill', clearable=False
    ),
    html.H6('Pie plot'),
    dcc.Graph(id='my-graph'),
])

@my_app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='drop-feature', component_property='value'),
     Input(component_id='drop-output', component_property='value')]
)
def displayPiePlot(feature, output):
    fig = px.pie(tips,
                 values=output,
                 names=feature
                 )
    return fig


my_app.run_server(
    port=8033,
    debug=True
)