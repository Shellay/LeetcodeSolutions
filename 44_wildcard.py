# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") 	--> false
# isMatch("aa","aa") 	--> true
# isMatch("aaa","aa") 	--> false
# isMatch("aa", "*") 	--> true
# isMatch("aa", "a*") 	--> true
# isMatch("ab", "?*") 		--> true
# isMatch("aab", "c*a*b") 	--> false

def match(word, pattern):
    """ Most easily do it like an NFA. """
    if word is pattern is '':
        return True
    elif word is '' or pattern is '':
        return False
    elif pattern[0] is '?' or word[0] == pattern[0]:
        return match(word[1:], pattern[1:])
    elif pattern[0] is '*':
        return \
            match(word[1:], pattern) or \
            match(word[1:], pattern[1:])
    else:
        return False

assert not match("aa","a")
assert match("aa","aa")
assert not match("aaa","aa")
assert match("aa", "*")
assert match("aa", "a*")
assert match("ab", "?*")
assert not match("aab", "c*a*b")

print('Test passed.')
