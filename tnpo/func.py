'''
3n + 1 Problem
--------------------
i. Statement
--------------------
The problem states that for any positive integer, n,
that perform i times of f(n) will eventually reach 1,
and stuck in (4, 2, 1) loop afterward.

--------------------
ii. Terminology
--------------------
parent - result of f(n)
child - arguably n itself

--------------------
1. Function
--------------------
Given function f(n), where n is integer > 0,
if n is odd, 3n + 1, else, n / 2.

--------------------
2. Sequence    
--------------------
Given function a(n), while n is not 4, n = f(n).
Assume that the problem statement is true, 
this a(n) is expected to stop at some point.

--------------------
3. Relationship
--------------------
Given function R(n), parent, n always has a child of 2n.
If n-1 is divisible by 3, then n also has a child of (n-1)/3.
'''

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

