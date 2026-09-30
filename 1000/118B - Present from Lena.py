"""
Problem: 118B - Present from Lena
Rating: 1000
Link: https://codeforces.com/problemset/problem/118/B

Idea:
The pattern is a symmetric rhombus.

For each row, print numbers increasing from 0 to i and then decreasing
from i - 1 back to 0.

The number of leading spaces is 2 * (n - i).

First print rows from 0 to n, then print rows from n - 1 back to 0
to create the lower half of the rhombus.
"""

n = int(input())

for i in range(n + 1):
    print(" " * (2 * (n - i)) + " ".join(map(str, list(range(i + 1)) + list(range(i - 1, -1, -1)))))

for i in range(n - 1, -1, -1):
    print(" " * (2 * (n - i)) + " ".join(map(str, list(range(i + 1)) + list(range(i - 1, -1, -1)))))
