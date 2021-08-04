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
def collatz_function(x):
    return x//2 if x%2 == 0 else linear(x)

# Collatz Conjecture
def collatz_conjecture(x):
    step, steps, hike, peak, peaks, height = [], 0, 0, [], 0, 0
    while x != 1:
        y = collatz_function(x)
        step.append(y)
        steps += 1
        if y > peak:
            hike = steps
            height = y
        else:
            peak.append(height)
            peaks += 1
        x = y
    return step, steps, hike, peak, peaks, height

