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
def sequence(n):
    step, steps = [], 0
    while n != 1:
        m = function(n)
        step.append(m)
        steps += 1
        n = m
    return step, steps

# Peak Function
'''
peak: Max spike value in sequence
step: No. of steps for sequence to reach peak
'''
def peak_func(ys, peak=0, step=0):
    if len(ys) > 0:
        peak = max(peak, ys[0])
        return peak_func(ys[1:], peak, step+1)
    else: return peak, step

# Spike Function
'''
spikes   : Spikes in sequence (^^^)
intervals: No. of steps between consecutive spikes
'''
def spike_func(ys, spikes=[], intervals=[], i=0):
    if len(ys) > 3:
        if ys[0]<ys[1]>ys[2]:
            spikes.append(ys[1])
            intervals.append(i)
            return spike_func(ys[3:], spikes, intervals)
        else: return spike_func(ys[1:], spikes, intervals, i+1)
    else: return spikes, intervals
