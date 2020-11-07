import urllib
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def parse_rowspan_table(table):
    """
    based on http://stackoverflow.com/a/28766684
    """

    tmp = table.find_all("tr")

    first = tmp[0]
    allRows = tmp[1:-1]

    headers = [header.get_text() for header in first.find_all("th")]

    results = [[data.get_text() for data in row.find_all("td")] for row in allRows]

    rowspan = []

    for no, tr in enumerate(allRows):
        for td_no, data in enumerate(tr.find_all("td")):
            if data.has_attr("rowspan"):
                rowspan.append((no, td_no, int(data["rowspan"]), data.get_text()))

    if rowspan:
        for i in rowspan:
            # tr value of rowspan in present in 1th place in results
            for j in range(1, i[2]):
                # Add value in next tr.
                results[i[0] + j].insert(i[1], i[3])

    return pd.DataFrame(data=results, columns=headers)


def ciaaw_atomic_masses():
    """
    Scrape the CIAAW webpage for atomic masses and return them as
    pandas DataFrame
    """

    url = "http://ciaaw.org/atomic-masses.htm"

    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, "html5lib")

    table = soup.find_all("table", attrs={"id": "mytable"})[0]
    df = parse_rowspan_table(table)

    df.loc[:, "Z"] = df["Z"].str.strip().astype(int)
    df.loc[:, "Element"] = df["Element"].str.strip()
    df.loc[:, "Symbol"] = df["Symbol"].str.strip("\t").astype(str)
    df.loc[:, "Atomic mass,ma/Da"] = df["Atomic mass,ma/Da"].str.strip()

    df.loc[:, "is_radioactive"] = df["A"].str.contains("*", regex=False)
    df.loc[:, "A"] = df["A"].str.extract("([0-9]+)", expand=False).astype(int)

    df.loc[:, "AM wows"] = df["Atomic mass,ma/Da"].str.replace("\s", "")
    df[["AM lead", "AM decimals", "AM unc"]] = df["AM wows"].str.extract(
        r"(\d+)\.(\d+)\((\d+)\)", expand=True
    )
    df["Atomic Mass"] = df["AM wows"].str.extract(r"(\d+\.\d+)", expand=False)

    # fill in the data for carbon
    df.loc[df["AM unc"].isnull(), "AM lead"] = 12
    df.loc[df["AM unc"].isnull(), "AM unc"] = 0

    # calculate the uncertainty
    mask = df["AM decimals"].notnull()
    dec = np.power(10, -1 * df.loc[mask, "AM decimals"].str.len().astype(float))
    df.loc[mask, "AM uncertainty"] = dec * df.loc[mask, "AM unc"].astype(int)

    df.loc[(df["Symbol"] == "C") & (df["A"] == 12), "Atomic Mass"] = 12.0e0
    df.loc[(df["Symbol"] == "C") & (df["A"] == 12), "AM uncertainty"] = 0.0e0
    df.loc[:, "Atomic Mass"] = df["Atomic Mass"].astype(float)

    df.drop("AM wows", axis=1, inplace=True)
    df.drop("AM lead", axis=1, inplace=True)
    df.drop("AM decimals", axis=1, inplace=True)
    df.drop("AM unc", axis=1, inplace=True)

    return df


def ciaaw_atomic_weights():
    """
    Scrape the CIAAW webpage for atomic weights and return them as
    pandas DataFrame
    """

    url = "http://ciaaw.org/atomic-weights.htm"

    table = pd.read_html(url, attrs={"id": "mytable"})[0]
    # drop the last row
    table = table.iloc[:-1, :]

    table = table.rename(columns={"Standard Atomic Weight": "SAW"})
    table.loc[:, "Z"] = table["Z"].astype(int)
    table.loc[:, "SAW"] = table["SAW"].str.replace("\s", "")
    table[["SAW decimals", "SAW unc"]] = table["SAW"].str.extract(
        r"\d+\.(\d+)\((\d+)\)", expand=True
    )

    # calculate the uncertainty
    mask = table["SAW decimals"].notnull()
    dec = np.power(10, -1 * table.loc[mask, "SAW decimals"].str.len().astype(float))
    table.loc[mask, "SAW uncertainty"] = dec * table.loc[mask, "SAW unc"].astype(int)

    table["Atomic Weight"] = (
        table["SAW"].str.extract(r"(\d+\.\d+)\(", expand=False).astype(float)
    )

    table.drop("SAW decimals", axis=1, inplace=True)
    table.drop("SAW unc", axis=1, inplace=True)

    return table


def ciaaw_isotopic_abundances():

    url = "http://ciaaw.org/isotopic-abundances.htm"

    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, "html5lib")

    table = soup.find_all("table", attrs={"id": "mytable"})[0]
    ia = parse_rowspan_table(table)

    abu = "Representative isotopic composition"
    ia.loc[:, "A"] = ia["A"].str.extract("([0-9]+)", expand=False).astype(int)
    ia.loc[:, "Z"] = ia["Z"].astype(int)
    ia.loc[:, abu] = ia[abu].str.replace("\s", "")
    ia.loc[:, "abundance"] = ia[abu].str.extract(r"(\d+\.\d+)\(", expand=False)
    ia.loc[:, "abundance"].fillna(
        ia[abu].str.extract(r"\[(\d+\.\d+),", expand=False), inplace=True
    )

    return ia


def ciaaw_monoisotopic():
    """
    Scrape the CIAAW webpage for monoisotopic elements and return the
    data as pandas DataFrame
    """

    url = "http://ciaaw.org/monoisotopic-elements.htm"

    # parse monoisotopic elements
    table = pd.read_html(url, attrs={"id": "mytable"})[0]
    # drop the last row
    table = table.iloc[:-1, :]
    # convert atomic number to integer
    table.loc[:, "Z"] = table.loc[:, "Z"].astype(int)
    return table
