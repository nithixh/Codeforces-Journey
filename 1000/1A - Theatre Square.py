"""
Problem: 1A - Theatre Square
Rating: 1000
Link: https://codeforces.com/problemset/problem/1/A

Idea:
We need to cover both dimensions of the square with flagstones of size a.

Number of flagstones needed along n = ceil(n / a)
Number of flagstones needed along m = ceil(m / a)

Since we cannot break flagstones, we round up whenever there is a remainder.

In integer arithmetic, ceil(x / a) can be calculated as:
(x + a - 1) // a

So the answer is the number needed along n multiplied by the
number needed along m.
"""

n, m, a = map(int, input().split())
x = (n + a - 1) // a
y = (m + a - 1) // a
print(x * y)
