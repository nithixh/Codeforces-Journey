"""
Problem: 745A - Hongcow Learns the Cyclic Shift
Rating: 900
Link: https://codeforces.com/problemset/problem/745/A

Idea:
Each cyclic shift moves the last character to the beginning.

Generate all possible cyclic shifts of the string and store
them in a set to avoid counting duplicates.

There are at most len(s) different shifts because after
len(s) shifts, the original string appears again.

The answer is the size of the set.
"""

s = input()
shifts = set()
for i in range(len(s)):
    shifts.add(s)
    s = s[-1] + s[:-1]
print(len(shifts))
