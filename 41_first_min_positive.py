# Problem: 
# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

inp = [1,2,3]

# Analysis:
#
# Thinking of pigeonhole principle...
#   -> Try to assign each positive number to its cardinal position; 
#   -> Find leftmost position which has no positive number.
#
#
# Implementation:
# 
# Case 1:
# if x > n,
# then x can't be answer
#
# Case 2:
# if x == n,
# then x is answer iff input can be ordered into
# a strict range [0..n-1]
#
# Case 3:
# if -1 < x < n:
# then x can be moved to the x'th position in the input array.
# so:
#   0. prepare a single slot for a number;
#   1. put number at x'th position into this box;
#   2. put x at x'th position;
#   3. repeat 1 until
#     -> number in the slot is identical to x
#        OR number in the slot is greater than n
#   4. iterate next.
#   
# Case 4:
# if x < 0:
# then just iterate next.
#
# Do one pass again, just to find first position
# at which the number doesn't equal its position.

def fir_mis_pos(inp):
    n = len(inp)
    n_seen = False
    for i in range(n):
        if inp[i] > n:
            inp[i] = -1
        elif inp[i] == n:
            n_seen = True ; inp[i] = -1
        elif inp[i] > -1: 
            b = inp[i]
            while -1 < b < n and b != inp[b]: # Also avoid self-loop.
                inp[b], b = b, inp[b]
        else:
            continue
    # After ordering, find first non-positive:
    for i in range(1, n):       # 0'th position is trivially ignored.
        if inp[i] != i:
            return i
    if n_seen: return n+1
    else: return n

inp1 = [1, 2, 0]
inp2 = [3, 4, -1, 1]

assert fir_mis_pos(inp1) == 3
assert fir_mis_pos(inp2) == 2

def inp_gen(n, noise=3):
    import random
    inp = list(range(n))
    for i in random.sample(range(n), noise):
        inp[i] = random.choice([-1, n+1, n+2, n+3])
    return inp

inp3 = inp_gen(20)
b = fir_mis_pos(inp3[:])
assert all(x in inp3 for x in range(1, b)) and b not in inp3

print('Test passed.')
