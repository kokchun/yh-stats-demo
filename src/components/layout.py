from dash.html import H1, Div, H2, Footer, H3, Span, Hr, Main, Section
from dash.dcc import Graph, Dropdown, Store, RadioItems
from components import years, category_dict
import components.filter_data, components.cards
from components.graphs import stats_graph


layout = Div(
    [
        Div(
            [
                H1("YH-statistik för data/IT-området"),
                Hr(),
            ],
            className="title-container",
        ),
        Section(
            [
                Div(
                    [
                        H2("Välj kategori"),
                        RadioItems(
                            [
                                {"label": label, "value": cateogry}
                                for cateogry, label in category_dict.items()
                            ],
                            value="Admitted students",
                            inline=True,
                            id="category-radio",
                        ),
                    ],
                    className="option",
                ),
                Div(
                    [
                        H2("Välj kön"),
                        RadioItems(
                            ["Män", "Kvinnor", "Totalt"],
                            "Totalt",
                            id="gender-radio",
                            inline=True,
                        ),
                    ],
                    className="option",
                ),
                Div(
                    [
                        H2("Välj år"),
                        Dropdown(years, 2022, id="year-dropdown", clearable=False),
                    ],
                    className="option",
                ),
            ]
        ),
        Main(
            [
                Div(
                    [
                        Div(
                            [H3("Antagna studerande"), Span(id="admitted-students")],
                            className="card",
                        ),
                        Div(
                            [H3("Antal studerande"), Span(id="students")],
                            className="card",
                        ),
                        Div(
                            [H3("Examinerade"), Span(id="graduated")], className="card"
                        ),
                        Div(
                            [H3("Examineringsgrad"), Span(id="graduation-rate")],
                            className="card",
                        ),
                    ],
                    className="cards-container",
                ),
                Graph(id="admission-graph"),
            ]
        ),
        Footer(
            "YH-studerande statistik, data hämtad från statistiska centralbyråns API 2023-08-08"
        ),
        Store(id="filter-df"),
    ],
    id="content-wrapper",
)
