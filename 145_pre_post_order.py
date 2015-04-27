# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?

class Node:
    def __init__(self, value, left=None, right=None): 
        self.value = value
        self.left = left
        self.right = right
        self.signal = 0
    def __repr__(self):
        return 'N{%s}' % self.value
    def is_leaf(self):
        return self.left is self.right is None
    def postorder(self):
        seq = []
        stk = [self] 
        while stk:
            p = stk.pop()
            if p.signal:
                seq.append(p)
            else:
                stk.append(p)
                if p.right:
                    stk.append(p.right)
                if p.left:
                    stk.append(p.left)
                p.signal = 1
        # Roll back modification of `signal.
        for _ in seq:
            _.signal = 0
        return seq
    def preorder(self):
        seq = []
        stk = [self] 
        while stk:
            p = stk.pop()
            seq.append(p)
            if p.right:
                stk.append(p.right)
            if p.left:
                stk.append(p.left)
        return seq
    def breadthorder(self): 
        seq = []
        que = [self]
        while que:
            p = que.pop(0)
            seq.append(p)
            if p.left: que.append(p.left)
            if p.right: que.append(p.right)
        return seq 

def read(tpl):
    """ Assume `tpl is organized in (v l r) manner. """
    if tpl: 
        return Node(tpl[0], read(tpl[1]), read(tpl[2]))
    else:
        return None

n3 = Node(3)
n2 = Node(2)
n1 = Node(1)
        
n1.right = n2
n2.left = n3

tpl = \
      (5,
       (3,
        (),
        (7,
         (),
         ()),),
       (4,
        (1,
         (),
         ()),
        (2,
         (),
         ())))

tree = read(tpl)
