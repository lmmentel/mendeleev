
from mendeleev import element


class Ion:

    '''

    # from the element get

    - atomic number
    - block
    - group
    - name
    - period
    - series
    - symbol

    '''

    def __init__(self, label, q):

        self.q = q

        self._set_element_properties(label)

    def _set_element_properties(self, label):

        e = element(label)
        self.Z = e.atomic_number
        self.block = e.block
        self.period = e.period
        self.mass = e.atomic_weight
        self.series = e.series
        self.group = e.group_id
        self.name = e.name
        self.symbol = e.symbol

        self.electrons = self.Z - self.q

        self.ie = e.ionenergies[self.q + 1]
        self.ea = e.ionenergies[self.q]

    @property
    def electrons(self):
        return self._electrons

    @electrons.setter
    def electrons(self):

        if abs(self.q) > self.Z:
            self._electrons = self.Z - self.q


    @property
    def ionic_potential(self):
        'Calculate the ionic potential'

        return self.q / self.radius
