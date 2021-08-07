from .func import *

'''
3n + 1 Problem
----------------
Statement
----------------
The problem states that for any positive integer, n,
that perform i times of f(n) will eventually reach 1,
and stuck in (4, 2, 1) loop afterward.

----------------
f(n) function
----------------
Given function f(n), where n is positive integer,
if n is odd, triple it and add one, else, halve it.

----------------
a(n) sequence
----------------
Given function a(n), while n is not 4, n = f(n).
If the problem statement is indeed true, 
this function will eventually stop at some point,
thus proving the statement through 'bruteforce' method.
'''

