# Palindrome Partitioning II 
# Given a string s, partition s such that every substring
# of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could
# be produced using 1 cut.

# ******************** APPROACH 1 ********************

# Key: There exists optimal substructure.
# Method: Dynamic Programming and Divide-&-Conquer
# -> Each palindrome can partition its host string into 3 parts.
# Let the 'heart' of the palindrome be h:
#   -1. left side of the palindrome L;
#   -2. the palindrome itself M;
#   -3. right side of the palindrome R;
#   *. Each palindrome with arbitrary length with h as its
#      heart can deliver such a partition.
#      
# -> L and R are both substrings, which should have there
#    mininum-cut calculated;
# -> Use Top-Down approach with memoization. 
#    *. How to convert into Bottom-Up approach?
# -> Since counting segments is easier than counting cuts,
#    count segments first.
# -> The Top-Down approach doesn't cover the construction-phase
#    of dynamic programming. 

from functools import wraps

def memo(f):
    lkp = {} 
    @wraps(f)
    def _f(*a): 
        if a not in lkp:
            lkp[a] = f(*a)
        return lkp[a]
    return _f

@memo
def min_segs_top_down(s, low, high):
    if low > high:
        return 0
    elif low == high:
        return 1
    elif low + 1 == high:
        if s[low] == s[high]: return 1
        else: return 2
    else:
        partis = []
        for p in range(low+1, high):
            if s[p] == s[p+1]:  # Handle even palindrome
                i = p ; j = p+1
                while low <= i and j <= high and s[i] == s[j]: 
                    partis.append([(low, i-1), (i, j), (j+1, high)])
                    i -= 1; j += 1
            else:               # Handle odd palindrome
                i = j = p
                while low <= i and j <= high and s[i] == s[j]: 
                    partis.append([(low, i-1), (i, j), (j+1, high)])
                    i -= 1; j += 1
                i = j = p + 1
                while low <= i and j <= high and s[i] == s[j]: 
                    partis.append([(low, i-1), (i, j), (j+1, high)])
                    i -= 1; j += 1
        best = float('inf')
        for (lw, a), m, (b, hi) in partis: 
            sub1 = min_segs_top_down(s, lw, a)
            sub2 = min_segs_top_down(s, b, hi)
            sub = sub1 + 1 + sub2
            if sub < best:
                best = sub
        return best

min_segs_top_down('aab', 0, 2)
# 2
min_segs_top_down('abcdcbe', 0, 6) 
# 3
min_segs_top_down('abcdcbebcdcba', 0, 12) 
# 1
min_segs_top_down('bcdcbebcdcba', 0, 11)
# 2


# ******************** APPROACH 2 ********************
# Now appeal for bottom-up approach!
# Consider induction:
# - We have optimal solution for length_1 string;
# - Suppose we have solution for length_N stirng;
#   -> Now augment a new character c to this string;
#      Try look backward for every possible palindrome ending with c: 
#      -> if any, then partit the augmented string with this
#         palindrome; 
#         we already know the solution of the left part that's
#         partited out, say y;
#         register y + 1 as the solution of the augemented string.
#   -> continue augmenting until exhausted.
# *. Since bottom-up approach is easier to implement, the following
#    implementation also contains the construction of solution, not
#    only finding optimal-value.

def is_palin(s, i, j):
    while i <= j:
        if s[i] != s[j]:
            return False
        else:
            i += 1 ; j -= 1
    return True

def min_cut(s):
    best = [None] * len(s) ; best[0] = 1
    solu = [None] * len(s) ; solu[0] = [(0, 0)] # inclusive both ends
    i = 1
    while i < len(best):
        best[i] = best[i-1] + 1
        solu[i] = solu[i-1] + [(i, i)]
        if is_palin(s, 0, i):
            best[i] = 1
            solu[i] = [(0, i)]
        else:
            j = 1
            while j < i:
                if is_palin(s, j, i) and best[j-1] + 1 < best[i]:
                    best[i] = best[j-1] + 1
                    solu[i] = solu[j-1] + [(j, i)]
                j += 1
        i += 1
    segs = [s[a:b+1] for a,b in solu[-1]]
    return best[-1]-1, segs

min_cut('aab') 
# (1, ['aa', 'b'])
min_cut('abcdcbe') 
# (2, ['a', 'bcdcb, 'e'])
min_cut('abcdcbebcdcba') 
# (0, ['abcdcbebcdcba'])
min_cut('bcdcbebcdcba')
# (1, ['bcdcbebcdcb', 'a'])
