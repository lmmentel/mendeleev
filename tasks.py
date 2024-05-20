from pathlib import Path
from invoke import task


@task
def export(c, format: str = "json"):
    """Export data to JSON files."""
    tables = [
        "elements",
        "groups",
        "ionicradii",
        "ionizationenergies",
        "isotopedecaymodes",
        "isotopes",
        "oxidationstates",
        "phasetransitions",
        "screeningconstants",
        "series",
    ]

    Path(f"data/{format}").mkdir(exist_ok=True)
    for table in tables:
        print(f"Exporting {table} to {format} ... ", end="")
        c.run(
            f"sqlite3 -{format} mendeleev/elements.db 'SELECT * FROM {table};' > data/{format}/{table}.{format}"
        )
        print("done")
