import tnpo

def test_f():
    assert tnpo.f(1) == 4
    assert tnpo.f(3, True) == 5

def test_R():
    assert tnpo.R(4) == {1, 8}
    assert tnpo.R(5, True) == {10, 3}

def test_a():
    assert tnpo.a(1) == [1]
    assert tnpo.a(3, True) == [3, 5, 8, 4, 2, 1]

