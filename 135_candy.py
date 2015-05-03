# Problem description:
# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?



# Keypoints and assumptions:
# - Suppose the first child has 1 candy;
# - Iterate pairwise (x1,x2) through the children;
#   -> if x1.value < x2.value, give x2 1 more candies than x1 has;
#   -> if x1.value > x2.value, give x2 1 less candies than x1 has;
#   -> if x1.value == x2.value, give x2 same candies as x1 has;
# - Resulted candy-sequence is a zigzag line of segments and  
#   each segment runs either ascendingly xor descendingly (nonstrictly);
# - Any other zigzag line with the same 'trend' is consistent
#   with the rule: lower-rating child has fewer candies than its neighbors;
# - So appealing for minimization of the area under this zigzag line
#   (which is exactly the total candy count), we try to find another
#   zigzag line ... 
#   We offset each monotone segment along negative y-direction, until its
#   lower end touches the threshold of candy number, say 1;
# - Resulted zigzag line is the solution of minimized candy count. 

# Implemetation details:
# - These mentioned above can be done in one pass;
# - Find turning points pairwise incrementally to determine the
#   segments inbetween with respect to the rating-values;
# - During the iteration, the previous turning point of zigzag line
#   is remembered, hence if we arrives at a new turning point,
#   the candies for children between these two turning points
#   are then incrementally assigned.

def candies(seq):
    N = len(seq)
    cand = [None] * len(seq)    # Simulate 'malloc'
    asc = True ; prv = 0
    for i in range(len(seq)): 
        if asc:
            if i+1 == N or seq[i] > seq[i+1]: # Now i is end OR i is turning point.
                asc = not asc 
                cand[prv] = 1
                for j in range(prv, i): # Assign candies for ascending segment (climb forwards).
                    cand[j+1] = cand[j] + \
                                (0 if seq[j] == seq[j+1] else 1)
                prv = i
        else:
            if i+1 == N or seq[i] < seq[i+1]:
                asc = not asc 
                cand[i] = 1
                for j in range(i-1, prv, -1): # Assign candies for descending segment (climb backwards).
                    cand[j] = cand[j+1] + \
                              (0 if seq[j] == seq[j+1] else 1)
                cand[prv] = max(cand[prv],
                                cand[prv+1]+1)
                prv = i
    return cand

# Basic test
children1 = [10, 11, 14,  9, 18, 13, 10,  5, 12, 15]
children2 = [14, 10,  5,  2,  3,  6,  7,  9,  8,  6]
children3 = [ 0,  0,  3,  3,  5,  5,  4,  0,  2,  2]

candies(children1)
# [1, 2, 3, 1, 4, 3, 2, 1, 2, 3]
candies(children2)
# [4, 3, 2, 1, 2, 3, 4, 5, 2, 1]
candies(children3)
# [1, 1, 2, 2, 3, 3, 2, 1, 2, 2]
