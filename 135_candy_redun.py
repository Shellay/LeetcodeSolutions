import pdb

# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Points:
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

def find_zigs(seq):
    """ zigs is a sequence of [a, b, a, b, ...], where
    [a:b] is ascending part, [b:a] is descending part.
    i.e. seq1[a] is peak, seq1[b] is bottom.
    """
    seq1 = [0] + seq + [0]
    asc = True ; spl = []
    for i in range(1, len(seq1)-1): 
        if asc:
            if seq1[i] > seq1[i+1]:
                asc = not asc
                spl.append(i)
        else:
            if seq1[i] < seq1[i+1]:
                asc = not asc
                spl.append(i)
    return seq1, [0] + spl + [len(seq1)-1]

def pairwise(seq):
    return zip(seq[::2], seq[1::2])

def candies(seq1, zigs):
    cand = [0] * len(seq1)
    for za, ze in pairwise(zigs):
        cand[za] = 1 if za > 0 else 0
        for j in range(za+1, ze+1): # j in [za+1 .. ze]
            if seq1[j-1] < seq1[j]:
                cand[j] = cand[j-1] + 1
            elif seq1[j-1] == seq1[j]:
                cand[j] = cand[j-1] 
            else: 
                assert 0, 'Wrong seq1'
    # pdb.set_trace()
    for zt, zb in pairwise(zigs[1:]): 
        cand[zb] == 1 if zb < len(seq1) - 1 else 0
        for j in range(zb, zt+1, -1): # j in [zb .. zt+1, stp=-1]
            if seq1[j-1] > seq1[j]:
                cand[j-1] = cand[j] + 1
            elif seq1[j-1] == seq1[j]:
                cand[j-1] = cand[j] 
            else:
                assert 0, 'Wrong seq1'
        cand[zt] = max(cand[zt], cand[zt+1]+1)
    return cand


seq = [10, 11, 14, 9, 18, 13, 10, 5, 12, 15]

seq1, zigs = find_zigs(seq)

c = candies(seq1, zigs)
