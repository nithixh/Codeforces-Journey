"""
Problem: 476A - Dreamoon and Stairs
Rating: 1000
Link: https://codeforces.com/problemset/problem/476/A

Idea:
Dreamoon can climb either 1 or 2 steps in each move.

Minimum possible moves = ceil(n / 2)
Maximum possible moves = n

Every number of moves between these limits is achievable.

We need the smallest multiple of m that is at least
the minimum possible moves.

Calculate this using ceiling division:
    ans = ((minimum + m - 1) // m) * m

If ans is greater than n, no valid answer exists.
Otherwise, print ans.
"""

n, m = map(int, input().split())
minimum = (n + 1) // 2
ans = ((minimum + m - 1) // m) * m
if ans <= n:
    print(ans)
else:
    print(-1)
