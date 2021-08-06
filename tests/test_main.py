from tnpo import *

def test_y():
    assert y(1) == 4
    assert y(2, 3, 4) == 10 

def test_f():
    assert f(1) == 4
    assert f(2) == 1

def test_s():
    assert s(3) == 5
    assert s(4) == f(4)

def test_a():
    assert a(1) == [1]
    assert a(3,s) == [3, 5, 8, 4, 2, 1]

def test_R():
    assert R(2) == {'n': 2, 'c': 4}
    assert R(4) == {'n': 4, 'c': 8, 'p': 1}

