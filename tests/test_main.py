import tnpo

def test_y():
    y = tnpo.y
    assert y(1) == 4
    assert y(2, 3, 4) == 10 

def test_f():
    f = tnpo.f
    assert f(1) == 4
    assert f(2) == 1

def test_s():
    f, s = tnpo.f, tnpo.s
    assert s(3) == 5
    assert s(4) == f(4)

def test_a():
    a, s = tnpo.a, tnpo.s
    assert a(1) == [1]
    assert a(2) == [2, 1]
    assert a(3,s) == [3, 5, 8, 4, 2, 1]

#def test_parent():
#    prnt = tnpo.parent
#    assert prnt(1) == 1
#    assert prnt(3) == 5
#    assert prnt(5) == 1
#
#def test_child():
#    chld = tnpo.child
#    assert chld(8) == 5
#    try: chld(2)
#    except tnpo.NoParentException(2): pass

