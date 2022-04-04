import dash as dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('CONVENIENT_global_confirmed_cases.csv')
df = df.dropna(axis=0, how='any')

col_name = []
df['China_sum'] = df.iloc[0:, 57:90].astype(float).sum(axis=1)
df['United Kingdom_sum'] = df.iloc[0:, 249:260].astype(float).sum(axis=1)

for col in df.columns:
    col_name.append(col)
df_covid = df[col_name]
df_covid['date'] = pd.date_range(start='1-23-20', end='11-22-20')

#dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

my_app = dash.Dash('my_app', external_stylesheets=external_stylesheets)

my_app.layout = html.Div([
    dcc.Graph(id = 'my-graph'),
    html.P('Pick the country name'),
    dcc.Dropdown(id='country',options=[
        {'label':'US', 'value':'US'},
        {'label':'Brazil', 'value':'Brazil'},
        {'label':'United Kingdom_sum', 'value':'United Kingdom_sum'},
        {'label':'China_sum', 'value':'China_sum'},
        {'label':'India', 'value':'India'},
        {'label':'Italy', 'value':'Italy'},
        {'label':'Germany', 'value':'Germany'},
    ], value='US', clearable=False)
])

@my_app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='country', component_property='value')]
)
def display_country(country):
    fig = px.line(df_covid, x='date', y=[country])
    return fig

my_app.run_server(
    port=8037,
    debug=True
)
