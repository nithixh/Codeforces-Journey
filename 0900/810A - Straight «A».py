"""
Problem: 810A - Straight «A»
Rating: 900
Link: https://codeforces.com/problemset/problem/810/A

Idea:
To get a rounded average of k, the actual average must be
at least k - 0.5.

To minimize additional marks, always add the maximum mark k.

Let x be the number of additional marks.

Required condition:
(total + x*k) / (n+x) >= k - 0.5

After rearranging:
x >= n*(2*k - 1) - 2*total

The answer is max(0, n*(2*k - 1) - 2*total).
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)
print(max(0, n * (2 * k - 1) - 2 * total))
