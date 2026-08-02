"""
Problem: 41A - Translation
Rating: 800
Link: https://codeforces.com/problemset/problem/41/A

Idea:
Reverse the second string and compare it with the first string. If they are
equal, the translation is correct; otherwise, it is incorrect.
"""

s=input()
t=input()
if t[::-1]==s:
    print("YES")
else:
    print("NO")
