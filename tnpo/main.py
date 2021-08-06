# Exceptions
class NoChildException(Exception):
    def __init__(self, parent):
        self.p = parent
        self.message = f'Number {parent} does not have a child.'
        super().__init__(self.message)

# Function
def y(x, m=3, c=1): return m*x+c # Linear
def e(n): return n%2==0 # Even

# 3n+1 Function
'''
n: {int n, n > 0}

f(n) = {n//2   , if n%2==0; 
        3n+1   , if n%2==1}

g(n) = {n//2   , if n%2==0; 
        3n+1//2, if n%2==1}
'''
def f(n): return n//2 if e(n) else y(n)
def g(n): return n//2 if e(n) else y(n)//2

# Sequence
'''
ai = {n      , for i=0;
      f(ai-1), for i>0}

i = len(seq) - 1
'''
def a(n):
    seq = [n]
    while n != 1:
        n = f(n)
        seq.append(n)
    return seq

# Node
def parent(c):
    p = 3*c+1
    while c%2==0: p//=2
    return p

def child(p):
    c = 2*p-1
    if c%3==0: return c//=3
    else: raise NoChildException(p)

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

