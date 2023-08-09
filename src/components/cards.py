from dash import callback, Input, Output
import pandas as pd 

@callback(
    Output("admitted-students", "children"),
    Output("students", "children"),
    Output("graduated", "children"),
    Output("graduation-rate", "children"),
    Input("filter-df", "data"),
    Input("year-dropdown", "value"),
)
def update_cards(data, year):
    df = pd.read_json(data)
    dff = df.loc[year]
    # print(df.loc[2022].to_list())
    return *dff.to_list()[:-1], f"{dff['Graduation rate']}%"
