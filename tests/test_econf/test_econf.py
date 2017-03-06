
from mendeleev.econf import ElectronicConfiguration


def test_parse():

    confs = ['1s', '1s2', '1s2 2s1', '1s2 2s2', '1s2 2s2 2p']
    ans = ['1s1', '1s2', '1s2 2s1', '1s2 2s2', '1s2 2s2 2p1']
    for c, a in zip(confs, ans):
        ec = ElectronicConfiguration(c)

        assert str(ec) == a
