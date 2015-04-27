# Word Break II
# Total Accepted: 28376 Total Submissions: 163842 
# Given a string s and a dictionary of words dict,
# add spaces in s to construct a sentence where each word
# is a valid dictionary word.

# Return all such possible sentences.

# For example, given
s = "catsanddog"
dic = ["cat", "cats", "and", "sand", "dog"]

# A solution is
["cats and dog", "cat sand dog"]

import itertools

def make_trie(dic):
    """ Use end symbol `$` to indicate a feasible word end position
    in trie. """
    trie = {}
    for wd in dic:
        wd += '$'
        sub = trie
        while 1:
            if wd[0] not in sub: sub[wd[0]] = {} 
            sub = sub[wd[0]]
            wd = wd[1:]
            if wd == '$':
                sub['$'] = '$'
                break;
    return trie

trie = make_trie(dic)
    
def find_fuzzy(rest, trie, path='', fuz=0): 
    if rest == '':
        # Ends at feasible position in trie??
        if '$' not in trie: return []
        else: return [path]
    else:
        res = []
        if '$' in trie:
            res.append(path)
        if rest[0] in trie:
            res.extend(find_fuzzy(rest[1:], trie[rest[0]],
                                  path=path+rest[0], fuz=fuz))
        if fuz > 0:
            # Including fuzzed search even if rest[0] is in trie,
            # i.e. search along its siblings in this case. 
            res.extend(f
                       for k in trie and k != rest[0]
                       for f in find_fuzzy(rest[1:], trie[k],
                                           path=path+k, fuz=fuz-1))
        return res
        
def fetch_word(rest, trie): 
    # if no word matched, return []
    ws = find_fuzzy(rest, trie)
    return [(w, rest[len(w):]) for w in ws]

def break_sentence(sent, trie):
    res = [] ; que = [[sent]]
    while que: 
        p = que.pop(0) ; sent = p.pop()
        if sent == '':
            res.append(p)
        else:
            ss = fetch_word(sent, trie) 
            for w,r in ss:
                que.append(p + [w,r])
    return [' '.join(_) for _ in res]

result = break_sentence(s, trie)

my_di = ['i', 'you', 'he', 'she',
         'walk', 'walks', 'am', 'walking',
         'lowly', 'slowly',
         'on', 'to', 'onto',
         'a', 'an',
         'exotical',
         'ship',
]

the_trie = make_trie(my_di)

his_sent = 'hewalkslowlyontoanexoticalship'
her_sent = 'shewalkslowlyontoanexoticalship'
your_sent = 'youwalkslowlyontoanexoticalship'

he = break_sentence(his_sent, the_trie) 
she = break_sentence(her_sent, the_trie) 
you = break_sentence(your_sent, the_trie) 
