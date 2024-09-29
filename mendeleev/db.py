"""Low-level database access functions."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine.base import Engine


DBNAME = "elements.db"


def get_package_dbpath() -> str:
    """Return the default database path"""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), DBNAME)


def get_engine(dbpath: str = None, read_only: bool = True) -> Engine:
    """Return the db engine"""
    if not dbpath:
        dbpath = get_package_dbpath()
    if read_only:
        connectstr = "sqlite:///file:{path:s}?mode=ro&nolock=1&uri=true".format(
            path=dbpath
        )
    else:
        connectstr = "sqlite:///{path:s}".format(path=dbpath)
    return create_engine(connectstr, echo=False)


def get_session(dbpath: str = None, read_only: bool = True) -> Session:
    """Return the database session connection."""
    engine = get_engine(dbpath=dbpath, read_only=read_only)
    db_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return db_session()
