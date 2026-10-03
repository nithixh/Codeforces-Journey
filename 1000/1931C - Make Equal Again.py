"""
Problem: 1931C - Make Equal Again
Rating: 1000
Link: https://codeforces.com/problemset/problem/1931/C

Idea:
Find the number of equal elements at the beginning and at the end.

If the first and last elements are equal, we can keep both the prefix
and suffix unchanged and only change the middle part.

If the first and last elements are different, we must change everything
except the larger equal prefix or suffix.

When the entire array contains the same value, the prefix and suffix
overlap, so the answer must be 0.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    left = 0
    while left < n and a[left] == a[0]:
        left += 1
    right = 0
    while right < n and a[n - 1 - right] == a[n - 1]:
        right += 1
    if a[0] == a[n - 1]:
        ans = n - left - right
    else:
        ans = n - max(left, right)
    print(max(0, ans))
