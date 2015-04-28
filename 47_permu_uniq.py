# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

# Concepts:
# The sequence as the ground set is grouped into groups of identical
# elements.
# - For each group, let m be the replication of grouped number;
# - For each i in [0 .. m-1], (i.e. i slots inbetween the group),
#   partit group into i+1 parts;
# - For each prepared permutation p, which is of length N, use i+1
#   parts to fill into some of the N+1 slots of p. 

def subsets(seq):
    """Iterative. Each subset is enumerated once with original
    order. Suppose `seq' has non-identical elements (even equality
    is treated as non-identical). """ 
    subseqs = [()]
    yield ()
    for x in seq: 
        nps = [_ + (x,) for _ in subseqs]
        yield from nps
        subseqs.extend(nps) 

# def comb(seq, m):
#     if m == 0: yield ()
#     elif m == len(seq): yield tuple(seq)
#     else:
#         yield from ((seq[0],) + _ for _ in comb(seq[1:], m-1))
#         yield from comb(seq[1:], m)

def combinations(seq, m): 
    N = len(seq)
    subcons = [((), -1)]
    for x in seq: 
        nps = []
        for subcomb, i in subcons:
            for j in range(i+1, N): # choose one from rest
                nps.append((subcomb + (seq[j],), j))
        if m == 0: break
        else: m -= 1
        subcons = nps
    for c, _ in subcons:
        yield c
    
def enum_two(seq):
    return zip(seq, seq[1:])

def split_with(seq, slti):
    """ `slti' is a sequence of indices, which is intended to be
    indices of the sequence of slots inbetween (no side slots)
    and split sequence `seq' into len(slti)+1 subsequences.
    E.g. [a,b,c,d,e], which is [a _0_ b _1_ c _2_ d _3_ e] with
    slots (0, 1, 2, 3), then some slti (1, 3) splits it into:
    [ [a,b], [c,d], [e] ]
    """
    if len(slti) == 0:
        yield seq[:]
    else:
        yield seq[:slti[0]+1] 		# seg-len: slti[0]+1
        for x, y in enum_two(slti):
            yield seq[x+1:y+1] 		# seg-len: y - x
        yield seq[slti[-1]+1:]		# seg-len: N - slti[-1] (seq[z:] == seq[z:N+1])

def partition(seq):
    if len(seq) == 1:
        # [ a ] -> [ [a] ]
        yield [seq]
    else:
        # [ a ] -> [ [a,b], [c,d,e], ... ]
        # slots: [0 .. n-2]:: [ a _0_ b _1_ c _2_ d ... ]
        slots = list(range(len(seq)-1)) 
        # Use each subset of slots to partit the sequence.
        # There're n-1 slots, thus 2**(n-1) slot-subsets. 
        for s in subsets(slots):
            yield list(split_with(seq, s))

def merge(seq_segs, partit):
    seqn = []
    for s, p in zip(seq_segs, partit + [[]]): 
        seqn.extend(s)
        seqn.extend(p)
    return seqn

def sepr_seq(seq, sgr):
    # The slot group `sgr' are considered to include side slots.
    # [ _0_ a0 _1_ a1 ... aN-1 _N_ ] i.e. ay is right of y (y is slot number)
    yield seq[:sgr[0]]
    for x, y in enum_two(sgr):
        yield seq[x:y]
    yield seq[sgr[-1]:]

def counter_sorted(seq):
    recs = []
    i = 0
    while i < len(seq):
        rec = [seq[i], 1]
        j = i + 1
        while j < len(seq) and seq[i] == seq[j]:
            # INVAR: Elements in [i, j) are identical.
            rec[-1] += 1 ; j += 1
        # INVAR: seq[i] != seq[j] and seq[i] == seq[j-1]
        recs.append(rec)
        i = j
    return recs 

def perm_uniq(seq):
    seq = sorted(seq)
    que = counter_sorted(seq)
    x, n = que.pop(0)
    perms = [ [x]*n ]
    for x, n in que:
        nperms = []
        for partit in partition([x] * n):
            for perm in perms:
                for sltgrp in combinations(tuple(range(len(perm)+1)),
                                           len(partit)): # partit is list
                    nperms.append(merge(sepr_seq(perm, sltgrp),
                                        partit))
        perms = nperms
    return perms

p = perm_uniq([1,1,2])
p = perm_uniq([1,1,2,2]) 		# Cardi: 4!/(2!*2!) == 6
p = perm_uniq([1,1,2,2,2,3]) 		# Cardi: 6!/(2!*3!*1!) == 60
