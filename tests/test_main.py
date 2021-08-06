from tnpo import *

def test_f():
    assert f(1) == 4
    assert f(3, True) == 5

def test_R():
    assert R(4) == {1, 8}
    assert R(5, True) == {10, 3}

def test_a():
    assert a(1) == [1]
    assert a(3, True) == [3, 5, 8, 4, 2, 1]

