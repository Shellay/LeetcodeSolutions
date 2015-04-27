import pdb

# Problem description:
# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Keypoints:
# - Suppose the first child has 1 candy;
# - Iterate pairwise (x,y) through the line of children;
#   -> if x.value < y.value, give y 1 more candy than x has;
#   -> if x.value > y.value, give y 1 less candy than x has;
#   -> if x.value == y.value, give y same candies as x has;
# - Resulted candy-sequence is a chained monotone segements of
#   lines which either go upwards xor downwards;
# - Find each 'trough' of the zig-zag line, offset it downwards
#   until bottom;
# - Resulted candy sequence is the solution.
# *. Gap can be strict-gap/semi-gap;
# *. Along iteration of children-rate-values, deliver a gap
#    each time when descending;

def candies(seq):
    seq1 = [0] + seq + [0]
    cand = [0] * len(seq1)
    asc = True ; prv = 1
    for i in range(1, len(seq1)-1): 
        if asc:
            if seq1[i] > seq1[i+1]:
                asc = not asc 
                cand[prv] = 1
                for j in range(prv, i+1): # Climb forwards...
                    cand[j+1] = cand[j] + \
                                (0 if seq1[j] == seq1[j+1] else 1)
                prv = i
        else:
            if seq1[i] < seq1[i+1]:
                asc = not asc 
                cand[i] = 1
                for j in range(i-1, prv, -1): # Climb backwords...
                    cand[j] = cand[j+1] + \
                              (0 if seq1[j] == seq1[j+1] else 1)
                cand[prv] = max(cand[prv],
                                cand[prv+1]+1)
                prv = i
    return cand

seq = [10, 11, 14, 9, 18, 13, 10, 5, 12, 15]

c = candies(seq)

c = c[1:-1]
