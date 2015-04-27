# Given a string s1, we may represent it as a binary tree by
# partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf
# node and swap its two children.

# For example, if we choose the node "gr" and swap its
# two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of
# nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length,
# determine if s2 is a scrambled string of s1.

def match(a, b):
    assert len(a) == len(b)
    if len(a) == 1:
        return a == b
    else:
        mid = len(a) // 2
        res1 = match(a[:mid], b[:mid]) and match(a[mid:], b[mid:]) or \
               match(a[:mid], b[-mid:]) and match(a[mid:], b[:-mid])
        res2 = False
        if len(a) & 1:
            mid += 1
            res2 = match(a[:mid], b[:mid]) and match(a[mid:], b[mid:]) or \
                   match(a[:mid], b[-mid:]) and match(a[mid:], b[:-mid])
        return res1 or res2 

# 
a = 'great'
b = 'rgtae'

match(a, b)

match('great', 'rgaet')
match('great', 'raget')
