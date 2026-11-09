"""
Problem: 989A - A Blend of Springtime
Rating: 900
Link: https://codeforces.com/problemset/problem/989/A

Idea:
For a cell to contain all three colours, its left neighbour,
itself, and its right neighbour must contain A, B, and C
in any order.

So, check every group of 3 consecutive characters.
If all three are different and none is '.', print Yes.

If no such group exists, print No.
"""

s = input()
possible = False
for i in range(len(s) - 2):
    a = s[i]
    b = s[i + 1]
    c = s[i + 2]
    if a != b and b != c and a != c and '.' not in (a, b, c):
        possible = True
        break
print("Yes" if possible else "No")
