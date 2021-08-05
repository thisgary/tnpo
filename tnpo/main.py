# common math functions
''' y = mx + c '''
def linear(x, m=3, c=1):
    return m*x + c

''' Long division by 2 '''
def ld2(x):
    return x if x%2 != 0 else ld2(x//2)

''' Is y 2 power n '''
def is_2n(y):
    return ld2(y) == 1
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

# 3n+1 problem sequence function
'''
step: No. of steps for sequence to reach 1
'''
def sequence(n):
    step = [n]
    while n != 1:
        n = function(n)
        step.append(n)
    return step

# Node function
'''
child : 
parent:  
'''
def node(child):
    if child%2 == 1: n = linear(child)
    parent = ld2(n)
    return parent

def draw_tree(nodes):
    nodes.sort()
    tree = []
    childs = []
    c_parent = 0
    for node in nodes:
        parent, child = node
        if len(childs) > 0:
            if parent == c_parent: childs.append(child)
            else:
                childs.sort()
                tree.append((parent,childs))
        else: c_parent, childs = parent, [child]
    return tree

