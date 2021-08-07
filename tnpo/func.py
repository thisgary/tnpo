'''
3n + 1 Problem
---------------
1. Function
---------------
Given n as any positive integer
f(n): if n even, n/2; else, 3n+1
'''
def f(n, s=False):
    m = 2 if s else 1
    return (3*n+1)//m if n%2 else n//2

def a(n, s=False):
    l = [n]
    while n != 1:
        n = f(n, s)
        l.append(n)
    return l

def ab(n):
    while n != 1:
        if n % 2: n = 3 * n + 1
        n //= 2

def R(n, s=False):
    c = {2*n}
    m = 2 if s else 1
    if n%(6//m) == 4//m:
        c.add((m*n-1)//3)
    return c

