import pandas as pd
from pathlib import Path

data_path = Path(__file__).parents[2] / "data"

yh_men = pd.read_csv(data_path / "yh_men.csv", index_col=0)
yh_women = pd.read_csv(data_path / "yh_women.csv", index_col=0)
yh_total = pd.read_csv(data_path / "yh_total.csv", index_col=0)

columns = yh_men.columns

category_dict = {
    "Admitted students": "Antagna studerande",
    "Students": "Antal studerande",
    "Graduates": "Examinerade",
    "Graduation rate": "Examineringsgrad",
}
years = yh_men.index
