from dash import Input, Output, callback
from components import yh_total, yh_men, yh_women


@callback(
    Output("filter-df", "data"),
    Input("gender-radio", "value"),
)
def filter_gender(gender):
    if gender == "Män":
        return yh_men.to_json()
    elif gender == "Kvinnor":
        return yh_women.to_json()
    else:
        return yh_total.to_json()
