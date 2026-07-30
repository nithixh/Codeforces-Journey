"""
Problem: 557A - Kitchen Utensils
Rating: 1000
Link: https://codeforces.com/problemset/problem/557/A

Idea:
Each complete utensil set is identical, so every utensil type must appear once
in every set. Count the maximum remaining frequency of any utensil type. The
minimum possible number of complete sets is the smallest multiple of k that is
at least this frequency. The difference between the original number of utensils
and the remaining utensils is the minimum number stolen.
"""

from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = Counter(a)

mx = max(cnt.values())
types = len(cnt)

sets = ((mx + k - 1) // k) * k

print(types * sets - n)
