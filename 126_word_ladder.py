# Word Ladder II 
# Given two words (start and end), and a dictionary,
# find all shortest transformation sequence(s) from start to end, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
import heapq
import functools

# Given:
start = "hit"
end = "cog"
dic = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]

# alpha = ''.join(chr(_) for _ in range(ord('a'), ord('z')+1))

def make_trie(dic):
    trie = {}
    for wd in dic:
        sub = trie
        while wd:
            if wd[0] not in sub: sub[wd[0]] = {} 
            sub = sub[wd[0]]
            wd = wd[1:]
    return trie
    
def find_fuzzy(rest, trie, path='', fuz=1): 
    if rest is '':
        return [path]
    else:
        res = []
        if rest[0] in trie:
            res += find_fuzzy(rest[1:], trie[rest[0]],
                              path=path+rest[0], fuz=fuz)
        if fuz > 0:       # including fuzzed even if rest[0] is in trie. 
            res += sum((find_fuzzy(rest[1:], trie[k],
                                    path=path+k, fuz=fuz-1)
                        for k in trie if k != rest[0]),
                        [])
        return res

def bfs(start, end, trie):
    exp = set() ; que = []
    qpush = lambda p: heapq.heappush(que, (len(p), p))
    qpop = lambda: heapq.heappop(que)[1]
    qpush([start])
    while que: 
        p = qpop() ; act = p[-1]
        if act in exp:
            continue
        else:
            exp.add(act)
            if act == end: return p
            else:
                nxt = find_fuzzy(act, trie)
                for n in nxt:
                    if n not in exp:
                        qpush(p + [n])
    return None

trie = make_trie(dic + [start, end])
