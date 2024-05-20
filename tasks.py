from pathlib import Path
from invoke import task


@task
def export(c):
    """Export data to a few formats files."""
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

    formats = [
        "csv",
        "html",
        "json",
        "markdown",
    ]

    for fmt in formats:
        Path(f"data/{fmt}").mkdir(exist_ok=True)
        for table in tables:
            print(f"Exporting {table} to {fmt} ... ", end="")
            c.run(
                f"sqlite3 -{fmt} mendeleev/elements.db 'SELECT * FROM {table};' > data/{fmt}/{table}.{fmt}",
                echo=True,
            )
            print("done")

    # SQL dump
    print("Creating SQL files with the data ... ", end="")
    c.run(
        "sqlite3 mendeleev/elements.db .dump > data/sql/elements.sql",
        echo=True,
        pty=True,
    )
    print("done")
