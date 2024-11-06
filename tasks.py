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
