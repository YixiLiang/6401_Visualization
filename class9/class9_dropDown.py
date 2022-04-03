import dash as dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

my_app = dash.Dash('My app', external_stylesheets=external_stylesheets)

my_app.layout = html.Div([
    html.H3('Complex Data Vis'),
    dcc.Dropdown(
        id='my-drop',
        options=[
            {'label': 'Introduction', 'value': 'Introduction'},
            {'label': 'Panda', 'value': 'Panda'},
            {'label': 'Seaborn', 'value': 'Seaborn'},
            {'label': 'Matplotlib', 'value': 'Matplotlib'}
        ],
        # value = 'Introduction' # default选项
        # multi=True  # 多选
        # searchable=False
        clearable=False
    ),
    html.Br(),
    html.Div(id='my-out')
])

@my_app.callback(
    Output(component_id='my-out', component_property='children'),
    [Input(component_id='my-drop', component_property='value')]
)

def Update_New(input):
    return f'The selected number is {input}'

# my_app.server.run(debug=True)
my_app.run_server(
    debug=True,
    port=8036,
)
