# 3n+1 problem statement
'''
n: int x > 0
'''

# Function
'''
f(n) = {n//2, if n mod 2 = 0; 
        3n+1, if n mod 2 = 1}
'''
def f(n):
    return n//2 if n%2==0 else 3*n+1

# Sequence
'''
ai = {n      , for i = 0;
      f(ai-1), for i > 0}

i: len(seq) - 1
'''
def a(n):
    seq = [n]
    while n != 1:
        n = f(n)
        seq.append(n)
    return seq

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

