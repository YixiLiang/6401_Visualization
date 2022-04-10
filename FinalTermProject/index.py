import pandas as pd
import numpy as np
import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("City", active=True, href="#")),
        dbc.NavItem(dbc.NavLink("Temperature", href="#")),
        dbc.NavItem(dbc.NavLink("Rain", href="#")),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
            label="Dropdown",
            nav=True,
        ),
    ]
)

# this example that adds a logo to the navbar brand
logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url('kangaroo.jpg'), style={'border-radius':'5px', 'margin-right':'10px'}, height="40px",width="40px")),
                        dbc.Col(dbc.NavbarBrand(children = [html.Font('Rain in Australia', className='fs-3', style={'font-style':'italic'})],className='ms-2')),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            nav,
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="dark",
    dark=True,
    className="mb-5",
    style={'margin':"0"}
)

carousel = dbc.Carousel(
    items=[
        {"key": "1",
         "src": 'https://images.pexels.com/photos/2845013/pexels-photo-2845013.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
         "header": "People Gathering Outside Sydney Opera House",
         "caption": 'Sydney, NSW, Australia',
         },
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


index_page = html.Div(children = [
    # html.Div(className='bg'),
    logo,
    html.Div(className='container', children=[
        dbc.Row(
            dbc.Col(
                html.Div('Rain in Australia', id='homePage-title'),
                width={"size": 6, "offset": 3},
            )
        ),
        dbc.Row(dbc.Col(html.Hr(style={'color':'000000FF', 'border':'1'}))),
        dbc.Row(
            dbc.Col(
                carousel
            )
        ),
        dbc.Row(dbc.Col(html.Div("Introduction", id='homePage-subtitle'))),
    ])
])


app.layout = html.Div(
    [index_page]
)


app.run_server(
    port=8033,
    debug=True
)


