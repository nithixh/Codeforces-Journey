"""
Problem: 344A - Magnets
Rating: 800
Link: https://codeforces.com/problemset/problem/344/A

Idea:
Each time the orientation of consecutive magnets changes, a new group starts.
Begin with one group for the first magnet, then compare each magnet with the
previous one. Increment the group count whenever the current orientation differs
from the previous.
"""

n = int(input())
prev = input()
groups = 1
for _ in range(n - 1):
    cur = input()
    if cur != prev:
        groups += 1
    prev = cur
print(groups)
