# common math functions
''' y = x^n '''
def is_power(y, x=2):
    while y%x == 0: y //= x
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
    step = s.index(peak)
    return peak, step

# Spike function
'''
spikes: Spikes in sequence (^^^)
steps : Steps between spikes
'''
def spike_func(s):
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
    return aux(s[:-3], [], [], 1)

