from pathlib import Path
from invoke import task


@task
def export(c, dest="data"):
    """Export data to a few formats files."""
    tables = {
        "elements",
        "groups",
        "ionicradii",
        "ionizationenergies",
        "isotopedecaymodes",
        "isotopes",
        "oxidationstates",
        "phasetransitions",
        "propertymetadata",
        "scattering_factors",
        "screeningconstants",
        "series",
    }

    formats = [
        "csv",
        "html",
        "json",
        "markdown",
    ]

    root = Path(f"{dest}")
    root.mkdir(exist_ok=True)

    for fmt in formats:
        path = root.joinpath(fmt)
        path.mkdir(exist_ok=True)
        for table in tables:
            print(f"Exporting {table} to {fmt} ... ", end="")
            c.run(
                f"sqlite3 -{fmt} mendeleev/elements.db 'SELECT * FROM {table};' > {path}/{table}.{fmt}",
                echo=True,
            )
            print("done")

    # SQL dump
    print("Creating SQL files with the data ... ", end="")
    path = root.joinpath("sql")
    path.mkdir(exist_ok=True)
    c.run(
        f"sqlite3 mendeleev/elements.db .dump > {path}/mendeleev.sql",
        echo=True,
        pty=True,
    )
    print("done")


def render_doc_table(class_name: str) -> str:
    """
    Fetch attributes for a specific class and render a table for documentation.
    """
    from mendeleev.utils import apply_rst_format, render_rst_table
    from mendeleev.fetch import fetch_table

    df = fetch_table("propertymetadata")
    df = df.loc[df["class_name"] == class_name]
    df = apply_rst_format(df)

    cols = ["Attribute name", "Description", "Unit", "Value origin", "Citation keys"]
    # display version of the column names
    return render_rst_table(df[cols].sort_values("Attribute name"))


def add_leading_spaces(multiline_string: str) -> str:
    "Add  three spaces in front of each line of a multiline string"
    lines = multiline_string.splitlines()
    modified_lines = [f"   {line}" if line.strip() else line for line in lines]
    return "\n".join(modified_lines)


def render_footnotes():
    "Render footnotes data in rst markup"
    from mendeleev.fetch import fetch_table

    df = fetch_table("propertymetadata")
    footnotes = ""
    for _, row in df[df["annotations"].notnull()].iterrows():
        footnote_mark = "[#f_" + row["attribute_name"] + "]"
        footnotes += f".. {footnote_mark} **{row['attribute_name']}**\n\n"
        notes = add_leading_spaces(row["annotations"])
        footnotes += f"{notes}\n\n"
    return footnotes


@task
def render_data_docs(c):
    """Render data documentation."""

    from jinja2 import Environment, FileSystemLoader

    env = Environment(
        loader=FileSystemLoader("docs/templates"),
    )

    template = env.get_template("data.rst")

    tables = {
        "Element": render_doc_table("Element"),
        "IonicRadius": render_doc_table("IonicRadius"),
        "IonizationEnergy": render_doc_table("IonizationEnergy"),
        "Isotope": render_doc_table("Isotope"),
        "IsotopeDecayMode": render_doc_table("IsotopeDecayMode"),
        "OxidationState": render_doc_table("OxidationState"),
        "PhaseTransition": render_doc_table("PhaseTransition"),
        "ScatteringFactor": render_doc_table("ScatteringFactor"),
        "ScreeningConstant": render_doc_table("ScreeningConstant"),
        "footnotes": render_footnotes(),
    }

    rendered = template.render(**tables)
    print(rendered)

    with open("docs/source/data.rst", "w") as f:
        f.write(rendered)


@task
def sqldiff(c, branch="master"):
    """Run sqldiff."""
    c.run(
        "git show master:mendeleev/elements.db > mendeleev/elements.db.master",
        echo=True,
    )
    c.run("sqldiff mendeleev/elements.db.master mendeleev/elements.db", echo=True)
