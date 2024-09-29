"""Utility functions for Mendeleev package."""

from typing import Union, Tuple
import math

import pandas as pd


def coeffs(a: int, b: int = 2) -> Tuple[int, int]:
    """
    Return stoichometric coefficients from oxidation states

    Args:
        a: oxidation state of the first element
        b: oxidation state  of the second element
    """
    lcm = abs(a * b) // math.gcd(a, b)
    return lcm // a, lcm // b


def n_effective(n: int, source: str = "slater") -> Union[float, None]:
    """
    Effective principal quantum number

    Args:
        n: Principal quantum number
        source: either `slater` or `zhang`, for more information see note below.

    .. note::

       Slater's values are taken from J. A. Pople, D. L. Beveridge,
       "Approximate Molecular Orbital Theory", McGraw-Hill, 1970

       Zhang's values are taken from Zhang, Y. (1982). Electronegativities
       of elements in valence states and their applications.
       1. Electronegativities of elements in valence states.
       Inorganic Chemistry, 21(11), 3886–3889. https://doi.org/10.1021/ic00141a005
    """
    numbers = {
        "slater": {1: 1.0, 2: 2.0, 3: 3.0, 4: 3.7, 5: 4.0, 6: 4.2},
        "zhang": {1: 0.85, 2: 1.99, 3: 2.89, 4: 3.45, 5: 3.85, 6: 4.36, 7: 4.99},
    }

    if source in numbers:
        return numbers.get(source).get(n)
    else:
        raise ValueError(
            f"source '{source}' not found, available sources are: {', '.join(numbers.keys())}"
        )


def render_rst_table(df: pd.DataFrame) -> str:
    """
    Converts a pandas DataFrame to a reStructuredText table.

    Args:
        df (pd.DataFrame): The DataFrame to convert.

    Returns:
        str: The DataFrame as a reStructuredText table.
    """
    # Get the column headers
    headers = df.columns.tolist()

    # Get the lengths of each column for formatting
    col_lengths = [
        max(len(str(val)) for val in df[col].tolist() + [col]) for col in headers
    ]

    # Create the horizontal line for the table
    hline = "+" + "+".join(["-" * (length + 2) for length in col_lengths]) + "+"
    header_hline = "+" + "+".join(["=" * (length + 2) for length in col_lengths]) + "+"

    # Format the header row
    header_row = (
        "|"
        + "|".join(
            [
                f" {headers[i]}{' ' * (col_lengths[i] - len(headers[i]))} "
                for i in range(len(headers))
            ]
        )
        + "|"
    )

    data_rows = []
    for _, row in df.iterrows():
        data_row = (
            "|"
            + "|".join(
                [
                    f" {str(row[col])}{' ' * (col_lengths[i] - len(str(row[col])))} "
                    for i, col in enumerate(headers)
                ]
            )
            + "|"
        )
        data_rows.extend((data_row, hline))
    return "\n".join([hline, header_row, header_hline] + data_rows)


def apply_rst_format(df: pd.DataFrame) -> pd.DataFrame:
    "Prepare daraframe for printing by intorducing ReST specific formatting"

    # convert the key to cite directive
    df.loc[:, "citation_keys"] = ":cite:`" + df["citation_keys"] + "`"

    # identify and add footnote_marks
    mask = df["annotations"].notnull()
    df.loc[mask, "footnote_mark"] = "[#f_" + df.loc[mask, "attribute_name"] + "]"
    df.loc[mask, "description"] = (
        df.loc[mask, "description"] + " (" + df.loc[mask, "footnote_mark"] + "_)"
    )

    # wrap attributes into code blocks
    df.loc[:, "attribute_name"] = "``" + df["attribute_name"] + "``"
    df.loc[:, "value_origin"] = df["value_origin"].str.lower()

    # capitalize column names which will be table headers
    df.columns = [c.replace("_", " ").capitalize() for c in df.columns]
    return df.fillna("")
