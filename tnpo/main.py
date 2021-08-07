# 3n+1 Problem Function
'''
n = 1, 2, 3...

f(n): if n even, halve it;
else, triple it and add 1. 

s(n): if n even, halve it;
else, f(n), then halve it. 
'''
def f(n, s=False):
    m = 2 if s else 1 # Shortcut
    return (3*n+1)//m if n%2 else n//2

# Relationship Function
'''
parent: n
child : f'(n)

- All parent has at least 1 child
- A parent can only have 1 child
- Odd parent can only have 1 child
'''
def R(n, s=False):
    c = {2*n} # Childs
    m = 2 if s else 1
    if n%(6//m)==4//m:
        c.add((m*n-1)//3)
    return c

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

