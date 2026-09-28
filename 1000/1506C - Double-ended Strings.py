"""
Problem: 1506C - Double-ended Strings
Rating: 1000
Link: https://codeforces.com/problemset/problem/1506/C

Idea:
Since we can only delete characters from the beginning or the end,
the remaining part of each string must be a continuous substring.

So, we need to find the longest common substring of a and b.

If its length is common, then:
- We delete len(a) - common characters from a.
- We delete len(b) - common characters from b.

Therefore, the minimum number of operations is:
len(a) + len(b) - 2 * common

We can simply check every substring of a and see if it occurs in b.
The string lengths are at most 20, so brute force is easily fast enough.
"""

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    common = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            sub = a[i:j]
            if sub in b:
                common = max(common, len(sub))
    print(len(a) + len(b) - 2 * common)
