import pandas as pd
import numpy as np
import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


#######################################
# common part
#######################################
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])





#######################################
# common part
#######################################
carousel = dbc.Carousel(
    items=[
        {"key": "1",
         "src": 'https://images.pexels.com/photos/68704/pexels-photo-68704.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
         "header": "Australia map",},
        {"key": "2",
         "src": "https://images.pexels.com/photos/995764/pexels-photo-995764.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "Aerial View of Sydney",
         "caption": 'Mosman, NSW, Australia',
         },
        {"key": "3",
         "src": "https://images.pexels.com/photos/533509/pexels-photo-533509.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "Group of People on Body of Water",
         },
        {"key": "4",
         "src": "https://images.pexels.com/photos/513799/pexels-photo-513799.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "High Rise Buildings",
         },
        {"key": "5",
         "src": "https://images.pexels.com/photos/2476154/pexels-photo-2476154.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
         "header": "Close-Up Photo of Grass During Golden Hour",
         "caption": 'Surfers Paradise, QLD, Australia',
         },
    ],
    controls=True,
    indicators=True,
    interval=2000,
    ride="carousel",
)

app.layout = html.Div([
    carousel
])



app.run_server(
    port=8041,
    debug=True
)