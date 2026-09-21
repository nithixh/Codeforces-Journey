"""
Problem: 131A - cAPS lOCK
Rating: 1000
Link: https://codeforces.com/problemset/problem/131/A

Idea:
If all characters except the first one are uppercase, the Caps Lock
was accidentally turned on.

For a single-character word, this condition is also considered true.

So, if s[1:] contains only uppercase letters, swap the case of the
entire string. Otherwise, leave it unchanged.
"""

s = input()
if s[1:].isupper() or len(s) == 1:
    print(s.swapcase())
else:
    print(s)
