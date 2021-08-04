# common math functions
''' y = x^n '''
def is_power(y, x=2):
    while y%x == 0: y //= x
    return y == 1

''' y = mx + c '''
def linear(x, m=3, c=1):
    return m*x + c

# 3n+1 Problem Statement
'''
f(n) = {n//2, x%2=0; 
        3n+1, x%2=1}

n: Any positive integer

If x is even, divide by 2,
if x is odd, 3x + 1.
'''
def function(x):
    return x//2 if x%2 == 0 else linear(x)

# 3n+1 Problem Sequence
'''
steps: No. of steps for sequence to reach 1
'''
def sequence(x):
    step, steps = [], 0
    while x != 1:
        y = function(x)
        step.append(y)
        steps += 1
        x = y
    return step, steps

'''
spike   : No. of spikes in sequence (^^^)
s_height: Value of spike
peak    : Max s_height in sequence
p_step  : No. of steps for sequence to reach peak

        if y > s_height: s_height = y
        else:
            spikes.append(s_height)
            spike += 1
            if s_height > peak:
                peak = s_height
                p_step = step
            s_height = 0
'''

