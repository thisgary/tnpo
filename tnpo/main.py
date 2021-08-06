# Function
def y(x, m=3, c=1): return m*x+c # Linear

# 3n+1 Problem Function
'''
n: {int n, n > 0}

f(n) = {n/2, if n%2=0; 
       3n+1, if n%2=1}

s(n) = {n/2, if n%2=0; 
     f(n)/2, if n%2=1}
'''
def f(n): return n//2 if n%2==0 else y(n)
def s(n): return n//2 if n%2==0 else y(n)//2

# Relationship Function
def R(n): 
    rel = {'n': n, 'c': 2*n}
    if n%6 == 4: rel['p'] = (n-1)//3
    return rel

# Sequence
'''
ai = {n, for i=0;
f(ai-1), for i>0}

i = len(seq) - 1
'''
def a(n, f=f):
    seq = [n]
    while n != 1:
        n = f(n)
        seq.append(n)
    return seq

def draw_tree(nodes):
    nodes.sort()
    tree, childs = [], []
    c_parent = 0
    for node in nodes:
        parent, child = node
        if childs:
            if parent == c_parent: childs.append(child)
            else:
                childs.sort()
                node = c_parent, childs
                tree.append(node)
                c_parent, childs = parent, [child]
        else: c_parent, childs = parent, [child]
    return tree

