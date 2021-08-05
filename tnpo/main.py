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
def peak_func(ys):
    def aux(xs, peak, p_step):
        if len(xs) > 0:
            peak = max(peak, xs[0])
            return aux(xs[1:], peak, p_step+1)
        else: return peak, step
    # Tail trimming [16, 8, 4, 2, 1]
    return aux(ys[:-5], 0, 0)

# Spike Function
'''
spikes: Spikes in sequence (^^^)
steps : Steps between consecutive spikes
'''
def spike_func(ys):
    def aux(xs, spikes, steps, i):
        if len(xs) > 2:
            a, b, c = xs[:3]
            if a < b > c:
                spikes.append(b)
                steps.append(i)
                xs, i = xs[1:], 1
            else: i += 1
            return aux(xs[1:], spikes, steps, i)
        else: return spikes, steps
    # Tail trimming [4, 2, 1]
    return aux(ys[:-3], [], [], 1)

