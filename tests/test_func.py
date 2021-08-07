import tnpo

def test_R():
    assert tnpo.R(2) == {4}
    assert tnpo.R(4) == {1, 8}

def test_a():
    assert tnpo.a(1) == [1, 4]
    assert tnpo.a(3) == [3, 10, 5, 16, 8, 4]

