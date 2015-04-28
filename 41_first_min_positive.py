# Problem: 
# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

inp = [1,2,3]

# Analysis:
# 
# Case 1:
# if x > n,
# then x can't be answer.
#
# Case 2:
# if x == n,
# then x is answer iff input can be ordered into
# a strict range [0..n-1]
#
# Case 3:
# if -1 < x < n:
# then x can be moved to the x'th position in input.
# so:
# 	0. prepare a box for one single number;
# 	1. put number at x'th position into this box;
# 	2. put x at x'th position;
# 	3. repeat 0 until
# 	  -> boxed number is identical to x
# 	  OR boxed number is greater than n
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
            y = inp[i]
            while -1 < y < n and y != inp[y]:
                b = inp[y]
                inp[y] = y
                y = b
        else:
            continue
    print('After ordering:\n', inp)
    for i in range(1, n):
        if inp[i] != i:
            return i
    if n_seen: return n+1
    else: return n

inp1 = [1, 2, 0]
inp2 = [3, 4, -1, 1]

def inp_gen(n, noise=3):
    import random
    # inp = [random.randint(-5, n+5) for _ in range(n)]
    inp = list(range(n))
    for i in random.sample(range(n), noise):
        inp[i] = random.choice([-1, n+1, n+2, n+3])
    return inp

inp3 = inp_gen(10)
inp4 = inp_gen(20)
inp5 = inp_gen(30)
