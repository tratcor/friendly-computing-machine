

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server=app.server

#df = pd.read_csv('X:/Current/Dev/Python/Visualisation Sandbox/UFO Sightings/ufo_sightings_scrubbed_small.csv')
df = pd.read_csv('X:/Current/Dev/Python/Visualisation Sandbox/UFO Sightings/ufo_sightings_scrubbed.csv', low_memory=False)
                 
fig = px.pie(df, values='count', names='country', title='UFO per Country', color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside', textinfo='percent+label')

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
