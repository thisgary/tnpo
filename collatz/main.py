# Common math functions used in Collatz conjecture
''' y = x^n '''
def is_power(y, x=2):
    while y%x == 0: y //= x
    return y == 1

''' y = mx + c '''
def linear(x, m=3, c=1):
    return m*x + c

# Collatz Function
'''
f(x) = {x//2, x%2=0; 
        3x+1, x%2=1}

x: Any positive integer

If x is even, divide by 2,
if x is odd, 3x + 1.
'''
def function(x):
    return x//2 if x%2 == 0 else linear(x)

# Collatz Sequence
'''
step    : No. of steps for sequence to reach 1
spike   : No. of spikes in sequence (^^^)
s_height: Value of spike
peak    : Max s_height in sequence
p_step  : No. of steps for sequence to reach peak
'''
def sequence(x):
    steps, spikes = [], []
    step, spike = 0, 0
    s_height = 0
    peak, p_step = 0, 0
    while x != 1:
        y = function(x)
        steps.append(y)
        step += 1
        if y > s_height: s_height = y
        else:
            spikes.append(s_height)
            spike += 1
            if s_height > peak:
                peak = s_height
                p_step = step
            s_height = 0
        x = y
    return steps, spikes, step, spike, peak, p_step

