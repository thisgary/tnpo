def f(n):
    return n*3+1 if n%2 else n//2

def a(n):
    s = (n,)
    while n != 4:
        n = f(n)
        s += (n,)
    return s

def R(n):
    c = {2*n}
    if n%6 == 4:
        c.add((n-1)//3)
    return c

