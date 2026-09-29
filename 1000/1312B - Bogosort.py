"""
Problem: 1312B - Bogosort
Rating: 1000
Link: https://codeforces.com/problemset/problem/1312/B

Idea:
Sort the array in decreasing order.

For i < j, the positions increase from left to right, while the values
in a decreasingly sorted array satisfy a[i] >= a[j].

Therefore, i - a[i] and j - a[j] cannot be equal, so the condition
for a good array is always satisfied.

Thus, simply sorting the array in descending order gives a valid answer.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(*a)
