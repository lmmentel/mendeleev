"""Low-level database access functions."""

import atexit
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine.base import Engine


DBNAME = "elements.db"


def get_package_dbpath() -> str:
    """Return the default database path"""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), DBNAME)


_engines: dict = {}


def _build_engine(dbpath: str, read_only: bool) -> Engine:
    if read_only:
        connectstr = "sqlite:///file:{path:s}?mode=ro&nolock=1&uri=true".format(
            path=dbpath
        )
    else:
        connectstr = "sqlite:///{path:s}".format(path=dbpath)
    return create_engine(connectstr, echo=False)


@atexit.register
def _dispose_engines() -> None:
    """Close pooled connections of all cached engines at interpreter exit."""
    for engine in _engines.values():
        engine.dispose()


def get_engine(dbpath: str = None, read_only: bool = True) -> Engine:
    """Return the db engine.

    Engines are cached per ``(dbpath, read_only)`` so that all callers share a
    single connection pool instead of leaking a new one on every call.
    """
    if not dbpath:
        dbpath = get_package_dbpath()
    key = (dbpath, read_only)
    if key not in _engines:
        _engines[key] = _build_engine(dbpath, read_only)
    return _engines[key]


def get_session(dbpath: str = None, read_only: bool = True) -> Session:
    """Return the database session connection."""
    engine = get_engine(dbpath=dbpath, read_only=read_only)
    db_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return db_session()
