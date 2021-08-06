# Exceptions
class NoOddChildException(Exception):
    def __init__(self, parent):
        log = f'Number {parent} does not have odd child.'
        super().__init__(log)

# Function
def y(x, m=3, c=1): return m*x+c # Linear

# 3n+1 Function
'''
n: {int n, n > 0}

f(n) = { n/2, if n%2=0; 
        3n+1, if n%2=1}

s(n) = {n/2, if n%2=0; 
     f(n)/2, if n%2=1}
'''
def f(n): return n//2 if n%2==0 else y(n)
def s(n): return n//2 if n%2==0 else y(n)//2

def R(n):
    while n%6 == 0: n //= 6
    n *= 2
    if n%6 != 4: return n
    else: return (n-1)//3

# Sequence
'''
ai = {n      , for i=0;
      f(ai-1), for i>0}

i = len(seq) - 1
'''
def a(n, f=f):
    seq = [n]
    while n != 1:
        n = f(n)
        seq.append(n)
    return seq

# Node
#def odd_parent(c):
#    p = c*3+1
#    while p%2==0: p//=1
#    return p
#
#def odd_child(p):
#    c = p*2-1
#    if c%3==0: return c//3
#    else: raise NoOddChildException(c)
#
# Dangerous as it enters infinite loop when p does not have a child
#def childs(p, n=1):
#    cs, c = [], p*2
#    while n > 0:
#        if (c-1)%3 == 0:
#            cs.append(c)
#            n -= 1
#        c *= 2
#    return cs

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

