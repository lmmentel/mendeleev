
from mendeleev.econf import ElectronicConfiguration


def test_parse():

    confs = ['1s', '1s2', '1s2 2s1', '1s2 2s2', '1s2 2s2 2p']
    ans = ['1s1', '1s2', '1s2 2s1', '1s2 2s2', '1s2 2s2 2p1']
    for c, a in zip(confs, ans):
        ec = ElectronicConfiguration(c)

        assert str(ec) == a


def test_largest_core():

    data = [
        ('1s', None),                       # H
        ('[He] 2s2', 'He'),                 # Be
        ('[Ne] 3s2 3p2', 'Ne'),             # Si
        ('[Ar] 3d10 4s2 4p4', 'Ar'),        # Se
        ('[Kr] 5s2', 'Kr'),                 # Sr
        ('[Xe] 4f14 5d10 6s2 6p4', 'Xe'),   # Po
        ('[Rn] 7s2', 'Rn')]                 # Ra

    for refconf, refcore in data:

        ec = ElectronicConfiguration(refconf)
        assert refcore == ec.get_largest_core()
