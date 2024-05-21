import pytest


def test_from_import():
    """Test that the main imports work"""
    from mendeleev import fetch

    assert fetch is not None
    from mendeleev import vis

    assert vis is not None
    from mendeleev import db

    assert db is not None
    from mendeleev import ion

    assert ion is not None
    from mendeleev import models

    assert models is not None
    from mendeleev import mendeleev

    assert mendeleev is not None


def test_direct_import():
    """Test that the main imports work"""
    import mendeleev.db  # noqa: F401
    import mendeleev.fetch  # noqa: F401
    import mendeleev.vis  # noqa: F401
    import mendeleev.ion  # noqa: F401
    import mendeleev.mendeleev  # noqa: F401
    import mendeleev.models  # noqa: F401


def test_missing_import():
    """Test that the import of a non-existing module raises ImportError"""
    with pytest.raises(ImportError):
        from mendeleev import nonexisting  # noqa: F401


def test_element_import():
    """Test that the element instances can be imported"""
    from mendeleev import C

    assert C is not None
