import requests
import pandas as pd
import polars as pl
from bs4 import BeautifulSoup
from bs4.element import Tag

from mendeleev.models import OxidationState
from mendeleev.db import get_session


def fetch_oxidation_states_table() -> Tag:
    "Fetch the table with oxidation states from wikipedia"

    url = "https://en.wikipedia.org/wiki/Oxidation_state"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        table_selector = "table.wikitable.sortable"

        if table := soup.select_one(table_selector):
            print("Table found and extracted!")
            return table
        else:
            print("Table not found with the specified CSS selector.")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")


def parse_oxidation_states_table(table: Tag) -> list[dict]:
    """
    Parse oxidation states from a table into a DataFrame.

    Args:
        table (bs4.element.Tag): The BeautifulSoup Tag object for the table.

    Returns:
        pd.DataFrame: A DataFrame with Z values as the first column and oxidation states from -5 to 9 as other columns.
    """
    parsed_rows = []

    for row in table.find_all("tr")[4:]:  # Skip the header rows
        # Extract the atomic number (Z value)
        z_value = row.find_all("td")[0].text.strip()
        if not z_value.isdigit():
            continue
        z_value = int(z_value)

        oxidation_states = {"Z": z_value}
        for i in range(-5, 10):
            oxidation_states[i] = None

        # iterate over oxidation state cells, starting from the 4th cell to the 18th
        for i, cell in enumerate(row.find_all("td")[3:18], start=-5):
            if cell.text.strip():
                if cell.find("b"):
                    oxidation_states[i] = True
                else:
                    oxidation_states[i] = False
        parsed_rows.append(oxidation_states)
    return parsed_rows


def create_pandas(data: list[dict]) -> pd.DataFrame:
    "Create a pandas dataframe"
    ox = pd.DataFrame(data)
    ox = (
        ox.melt(id_vars=["Z"], value_vars=list(range(-5, 10)))
        .dropna(axis="rows", subset=["value"])
        .sort_values(by="Z")
        .reset_index(drop=True)
    )
    ox.loc[:, "category"] = ox.value.map({True: "main", False: "extended"})
    return ox.rename(
        columns={"Z": "atomic_number", "variable": "oxidation_state"}
    ).drop(columns=["value"], axis="columns")


def create_polars(data: list[dict]) -> pl.DataFrame:
    "Create a polars dataframe"
    parsed_str = [{str(k): v for k, v in d.items()} for d in data]
    ox = pl.from_dicts(parsed_str)
    return (
        ox.melt(id_vars=["Z"])
        .drop_nulls(subset=["value"])
        .rename(
            {"Z": "atomic_number", "variable": "oxidation_state", "value": "category"}
        )
        .cast({"oxidation_state": pl.Int32})
        .with_columns(pl.col("category").map_dict({True: "main", False: "extended"}))
    )


if __name__ == "__main__":
    table = fetch_oxidation_states_table()
    parsed = parse_oxidation_states_table(table)
    ox = create_pandas(parsed)

    update = False
    if update:
        session = get_session(read_only=False)
        objects = [
            OxidationState(
                atomic_number=row["atomic_number"],
                oxidation_state=row["oxidation_state"],
                category=row["category"],
            )
            for i, row in ox.iterrows()
        ]
        session.add_all(objects)
        session.commit()
        session.close()
