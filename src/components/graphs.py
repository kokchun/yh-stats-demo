import plotly.graph_objects as go
from dash import Input, Output, callback
import pandas as pd
from components import category_dict

base_layout = dict(
    template="simple_white",
    paper_bgcolor="rgba(238,238,238)",
    xaxis=dict(linecolor="rgba(0,0,0,.4)", color="rgba(0,0,0,.5)"),
    yaxis=dict(linecolor="rgba(0,0,0,.4)", color="rgba(0,0,0,.5)"),
    hovermode="x unified",
    showlegend=False,
    xaxis_title = "År",
    margin=dict(l=0,r=0,t=40,b=30),
)

@callback(
    Output("admission-graph", "figure"),
    Input("filter-df", "data"),
    Input("gender-radio", "value"),
    Input("category-radio", "value"),
)
def stats_graph(data, gender, category):
    df = pd.read_json(data).replace(0, pd.NA)

    fig = go.Figure(
        data=dict(x=df.index, y=df[category]),
        layout=dict(title=f"{category_dict[category]} {gender.lower()} inom området data/IT", **base_layout),
    )
    return fig


# TODO: different titles, ylabels