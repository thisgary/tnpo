# common math functions
''' y = x^n '''
def is_power(y, x=2):
    while x%2 == 0: y //= x
    return y == 1

''' y = mx + c '''
def linear(x, m=3, c=1):
    return m*x + c

# 3n+1 problem function
'''
f(n) = {n//2, x%2=0; 
        3n+1, x%2=1}

n: Any positive integer

If x is even, divide by 2,
if x is odd, 3x + 1.
'''
def function(x):
    return x//2 if x%2 == 0 else linear(x)

# 3n+1 problem sequence
'''
step: No. of steps for sequence to reach 1
'''
def sequence(n):
    step = [n]
    while n != 1:
        n = function(n)
        step.append(n)
    return step

# Peak function
'''
peak: Max value in sequence
step: No. of steps for sequence to reach peak
'''
def peak_func(s):
    peak = max(s)
    step = s.index(peak) - 1
    return peak, step

# Odd function
'''
odds: Odd numbers in sequence (^^^)
'''
def odd_func(s):
    odds = []
    while len(s) > 0:
        n, s = s[0], s[1:]
        if y%2 == 1:
            odds.append(n)
            s = s[1:]
    return odds
 
