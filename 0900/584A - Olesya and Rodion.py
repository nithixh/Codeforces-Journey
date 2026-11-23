"""
Problem: 584A - Olesya and Rodion
Rating: 1000
Link: https://codeforces.com/problemset/problem/584/A

Idea:
We need an n-digit number divisible by t.

There are two cases:

1. If t != 10:
   A number consisting of n copies of digit t is always
   divisible by t.

2. If t == 10:
   The number must end in 0.
   - If n == 1, no valid number exists, so print -1.
   - Otherwise, print n-1 ones followed by a zero.

Both constructions produce an n-digit number divisible by t.
"""

n, t = map(int, input().split())
if t == 10:
    if n == 1:
        print(-1)
    else:
        print("1" * (n - 1) + "0")
else:
    print(str(t) * n)
