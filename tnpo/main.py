# 3n+1 Problem Function
'''
n = 1, 2, 3...

f(n): if n even, halve it;
else, triple it and add 1. 

s(n): if n even, halve it;
else, f(n), then halve it.      
'''
def f(n, s=False):
    if n % 2 == 0: return n//2
    else:
        n = n * 3 + 1
        if s: n //= 2
        return n

# Relationship Function
def R(n, s=False):
    c = 2 * n # Child
    r = { c }
    m = 2 if s else 1
    if n % (6 // m) == 4 // m:
        p = (m * n - 1) // 3
        r.add(p) # Parent
    return r

# Sequence Function
'''
a(n) = while n not 1, append f(n)
'''
def a(n, s=False):
    l = [n]
    while n != 1:
        n = f(n, s)
        l.append(n)
    return l

