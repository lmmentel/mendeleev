from mendeleev.db import get_engine
from sqlalchemy import text as sql_text
import pandas as pd


def test_read_sql_table():
    engine = get_engine()
    query = "select * from elements"
    with engine.begin() as conn:
        df = pd.read_sql_query(sql=sql_text(query), con=conn)
    assert df is not None


def test_read_sql_table_old():
    engine = get_engine()
    query = "select * from elements"
    # with engine.begin() as conn:
    conn = engine.connect()
    df = pd.read_sql_query(sql=query, con=conn)
    assert df is not None
