def match(word, pattern):
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
