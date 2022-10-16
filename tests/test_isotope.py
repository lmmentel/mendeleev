from mendeleev import isotope


def test_get_isotope():

    # Hydrogen
    result = isotope(1, 1)
    assert result.atomic_number == 1
    assert result.mass_number == 1

    result = isotope("H", 3)
    assert result.atomic_number == 1
    assert result.mass_number == 3