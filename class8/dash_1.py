import dash as dash
from dash import dcc
from dash import html





my_app = dash.Dash('My app')

my_app.layout = html.Div([
                html.Div(html.H1("Hello world! with html.H1")),
                html.Div(html.H2("Hello world! with html.H2")),
                html.Div(html.H3("Hello world! with html.H3")),
                html.Div(html.H4("Hello world! with html.H4")),
                html.Div(html.H5("Hello world! with html.H5")),
                html.Div(html.H6("Hello world! with html.H6")),
                ])
my_app.server.run(
    port = 8100,
    host = '0.0.0.0'
)

