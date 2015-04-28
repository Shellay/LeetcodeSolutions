# Input:

# There are multiple test cases!
# The input consists of N pairs of integers, where 1 < N < 700. Each pair of integers is separated by one blank and ended by a new-line character. The list of pairs is ended with an end-of-file character. No pair will occur twice. 
# The input ends with a case which N is equal to zero
# Output:

# The output consists of one integer representing the largest number of points that all lie on one line.
# Sample Input:

# 5
inp = """1 1
2 2
3 3
9 10
10 11"""
# Sample Output: 
# 3

inp1 = """1 1
2 2
3 3
9 10
10 11
2 5
3 6
4 7
5 8"""
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6"""

inp2 = """1 1
2 2
3 3
9 10
10 11
2 5
3 6
4 7
5 8
1 2
1 3
1 4
1 5
1 6"""

def prep(inp):
    return [tuple(int(_) for _ in l.split())
            for l in inp.splitlines()]

def slope(p1, p2):
    x1, y1 = p1 ; x2, y2 = p2
    if x1 == x2:
        return None
    else:
        return round((y2 - y1) / (x2 - x1), 3)

def line(p1, p2):
    k = slope(p1, p2)
    x1, y1 = p1
    b = round(y1 - k * x1, 3) if k != None else x1
    return (k, b)

from collections import defaultdict
# def cons_map(ps):
#     ps = sorted(ps, key=lambda p:p[-1]) 
#     ks = {}
#     seen = { ps.pop(0) }
#     while ps:
#         p = ps.pop(0) 
#         for pi in seen:
#             k = slope(p, pi) 
#             if k not in ks:
#                 ks[k] = { pi : {p} }
#             else:
#                 for p1 in ks[k]:
#                     if slope(p, p1) == k:
#                         ks[k][p1].add(p) 
#         seen.add(p)
#     return ks
    
# def find_max(m):
#     return max(({p} | ps
#                 for p_ps in mp.values()
#                 for p, ps in p_ps.items()), key=len)
def cons_lines(ps):
    mp = defaultdict(set)
    for i in range(len(ps)-1):
        for j in range(i+1, len(ps)): 
            k, b = line(ps[i], ps[j]) 
            mp[(k,b)].add(ps[i])
            mp[(k,b)].add(ps[j])
    return mp

def find_max(mp):
    return max(mp.values(), key=len)

ps = prep(inp1)
mp = cons_lines(ps)
result = find_max(mp)
