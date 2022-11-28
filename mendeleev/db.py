import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine.base import Engine


DBNAME = "elements.db"


def get_package_dbpath() -> str:
    """Return the default database path"""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), DBNAME)


def get_engine(dbpath: str = None) -> Engine:
    """Return the db engine"""
    if not dbpath:
        dbpath = get_package_dbpath()
    return create_engine("sqlite:///{path:s}".format(path=dbpath), echo=False)


def get_session(dbpath: str = None) -> Session:
    """Return the database session connection."""
    engine = get_engine(dbpath=dbpath)
    db_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return db_session()
