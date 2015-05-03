# Minimum Window Substring
# Total Accepted: 30731 Total Submissions: 163783 
# Given a string S and a string T, find the minimum window in S
# which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T,
# return the emtpy string "".

# If there are multiple such windows, you are guaranteed that there
# will always be only one unique minimum window in S.


# Keys:
# 1. Find indices of characters from T in S;
# 2. These index of each character is grouped into a sequence;
# 3. Pop the first group from such sequence, transform it into singleton
#    interval-form;
# 4. Prepare a queue to contain all sufficient-intervals;
# 5. Pop the next group, use the indices to augment current intervals
#    such that each augmented interval can cover all characters so far;
#    -> For each index of the new character,
#        -> if it's covered by a current interval, then register this interval;
#        -> otherwise:
#            -> if there's no other index between it and the nearest left 
#               interval, then register this interval's augmented version;
#            -> same for the nearest right interval

from itertools import product

def table(s, t):
    lkp = {k:[] for k in t}
    for i, c in enumerate(s): 
        if c in lkp:
            lkp[c].append(i)
    return lkp 

def brutal(s, t):
    lkp = table(s, t)
    ps = product(*lkp.values())
    p = min(ps, key=lambda p:max(p)-min(p))
    i, j = min(p), max(p)
    return s[i:j+1], [i, j]

def queue_merge(intvs, seq):
    i = j = 0
    que = []
    while i < len(intvs): 
        if intvs[i][1] >= seq[j]:
            # This happens only if intvs[i].right >= seq[j]
            curr = intvs[i][:] ; m = False
            while j < len(seq) and seq[j] < curr[1]:
                if seq[j] < intvs[i][0]:
                    # Compress useful interval
                    curr[0] = seq[j]
                else:
                    # Confirm deliverance of interval
                    curr[0] = intvs[i][0]
                    m = True
                j += 1
            que.append(curr)
            if j == len(seq):
                # Now seq is exhausted, no more new intervals possible.
                break
            else:
                # Now seq[j] is the first greater than intvs[i].right
                # Iterate through intvs until the first is over seq[j]
                while i < len(intvs) and intvs[i][1] < seq[j]: 
                    i += 1 
                if not m:
                    que.append([intvs[i-1][0], seq[j]])
        else:
            i += 1
    return que 

def augment(intvs, seq):
    i = j = 0
    que = []
    while i < len(intvs):
        while j < len(seq) and seq[j] < intvs[i][0]:
            j += 1
        # Now either j == len(seq) xor intvs[i][0] <= seq[j]
        if j == len(seq): 
            if 0 < j and (0 == i or intvs[i-1][0] < seq[j-1]):
                que.append([seq[j-1], intvs[i][1]])
                break
        elif j < len(seq) and intvs[i][0] <= seq[j] <= intvs[i][1]: 
            que.append(intvs[i])
        else:
            if 0 < j and (0 == i or intvs[i-1][0] < seq[j-1]):
                que.append([seq[j-1], intvs[i][1]])
            if j < len(seq) and (i == len(intvs)-1 or seq[j] < intvs[i+1][1]):
                que.append([intvs[i][0], seq[j]])
        i += 1
        # If now i == len(intvs), then the rest seq part cannot
        # contribute new useful intervals, so the loop ends.
    return que

def min_win(S, T):
    items = iter(table(S, T).values())
    # Singleton interval.
    intvs = [[_,_] for _ in next(items)]
    for item in items:
        # intvs = queue_merge(intvs, item)
        intvs = augment(intvs, item)
    i, j = min(intvs, key=lambda p:p[1] - p[0])
    return S[i:j+1], [i, j]

# basic test
# a = [5,9,15,20]
# b = [3,4,8,16,19]
# c = [6, 12, 24]
# s = "adobecodebanc"
# t = "abc" 
# brutal(s, t)

# a_intv = [[_, _] for _ in a] 
# queue_merge(a_intv, b)
# ab = augment(a_intv, b)
# abc = augment(ab, c)
# min_win(s, t)

import random 

def gen_str(ground='abcdefghi', n=100):
    sqn = ''.join(random.choice(ground) for _ in range(n)) 
    return sqn

sqn = 'dcbeggceedeecddggbcafdgfcaadeggbcafdafbagbcgedcdegagdagedfbcfbbeefaadfgbeccagbafcafcdgebaeafgfafcdgc'
p = brutal(sqn, 'abcde')
q = min_win(sqn, 'abcde')

assert p == q

print('Test passed.')

brutal(s, 'abcde')
min_win(s, 'abcde')
