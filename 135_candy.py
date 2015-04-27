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
    asc = True ; last_turning = -1
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

seq = [10, 11, 14, 9, 18, 13, 10, 5, 12, 15]

seq1, zigs = find_zigs(seq)

c = candies(seq1, zigs)
