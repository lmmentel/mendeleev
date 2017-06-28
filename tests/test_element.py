

import pytest
from mendeleev import get_session, Element, element


@pytest.fixture
def session():

    return get_session()


def test_querry(session):

    si = session.query(Element).filter(Element.symbol == 'Si').one()
    assert si.name == 'Silicon'


def test_element():

    si = element('Si')
    assert si.name == 'Silicon'
