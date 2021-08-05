# common math functions
''' Long division by 2 '''
def ld2(x):
    return x if x%2 != 0 else ld2(x//2)

''' Is y 2 power n '''
def is_2n(y):
    return ld2(y) == 1

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
step: No. of steps to reach peak
'''
def peak_func(s):
    peak = max(s)
    step = s.index(peak) - 1
    return peak, step

# Next cycle
def halt(n):
    n = function(n)
    return ld2(n)

