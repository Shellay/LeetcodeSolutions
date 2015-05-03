# Interleaving String
# Total Accepted: 29676 Total Submissions: 144340

# Given s1, s2, s3, find whether s3 is formed by the interleaving
# of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.


# Keys:
# This is somewhat like the merge-phase of mergesort;
# Use two queues q1 and q2 to represent s1 and s2;
# Use a queue q to represent s3;
# Peek q3, then fetch the peeked by dequeueing q1 or q2,
#   case 1: q1.peek() != q2.peek()
#           if q1.peek() == q3.peek(): q1.deque() ; q3.deque()
#           elif q2.peek() == q3.peek(): q2.deque() ; q3.deque()
#           else: report(False)
#   case 2: q1.peek() == q2.peek()
#           Branch the searching!

def check_interleaving(s1, s2, s3):
    stk = [(s1, s2, s3)]
    while stk:
        q1, q2, q = stk.pop()
        if q1 == q2 == q == '':
            return True
        elif q1 == '':
            if q2[0] == q[0]:
                stk.append(('', q2[1:], q[1:]))
        elif q2 == '':
            if q1[0] == q[0]:
                stk.append((q1[1:], '', q[1:]))
        else:
            if q1[0] == q2[0]: 
                if q1[0] == q[0]:
                    stk.append((q1[1:], q2, q[1:]))
                    stk.append((q1, q2[1:], q[1:]))
            else:
                if q1[0] == q[0]:
                    stk.append((q1[1:], q2, q[1:]))
                elif q2[0] == q[0]:
                    stk.append((q1, q2[1:], q[1:]))
    return False

def check_index(s1, s2, s3):
    stk = [(0, 0, 0)]
    while stk:
        i, j, k = stk.pop()
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        elif i == len(s1):
            if s2[j] == s3[k]:
                stk.append((i, j+1, k+1))
        elif j == len(s2):
            if s1[i] == s3[k]:
                stk.append((i+1, j, k+1))
        else:
            if s1[i] == s2[j]: 
                if s1[i] == s3[k]:
                    stk.append((i+1, j, k+1))
                    stk.append((i, j+1, k+1))
            else:
                if s1[i] == s3[k]:
                    stk.append((i+1, j, k+1))
                elif s2[j] == s3[k]:
                    stk.append((i, j+1, k+1))
    return False

import random
def gen_interleave(gset, bias=.5):
    s1 = [] ; s2 = [] 
    for c in gset:
        if random.random() < bias:
            s1.append(c)
        else:
            s2.append(c)
    return ''.join(s1), ''.join(s2)

# Basic case:
# s1 = 'aabcc'
# s2 = 'dbbca' 
# s3 = 'aadbbcbcac' # , return true.
# s4 = 'aadbbbaccc' # , return false. 
# check_interleaving(s1, s2, s3)
# check_interleaving(s1, s2, s4) 
# check_index(s1, s2, s3)
# check_index(s1, s2, s4)

s3 = 'abcdefghhiijjjkkklmnopq'
s1, s2 = gen_interleave(s3)
check_interleaving(s1, s2, s3)
check_index(s1, s2, s3)
