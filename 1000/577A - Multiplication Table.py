"""
Problem: 577A - Multiplication Table
Rating: 1000
Link: https://codeforces.com/problemset/problem/577/A

Idea:
The cell at row i and column j contains i * j.

For each row i from 1 to n, check whether x is divisible by i.
If it is, calculate j = x // i.

The value x appears in that row only if j is between 1 and n.
Count every such valid occurrence.

Since the table is symmetric, different valid rows can give
different cells containing x.
"""

n, x = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    if x % i == 0:
        j = x // i
        if 1 <= j <= n:
            ans += 1
print(ans)
