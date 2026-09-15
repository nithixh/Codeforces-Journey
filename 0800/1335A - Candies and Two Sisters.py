"""
Problem: 1335A - Candies and Two Sisters
Rating: 800
Link: https://codeforces.com/problemset/problem/1335/A

Idea:
Alice must get more candies than Betty, so Betty can receive
any number from 1 up to just below n/2.

If n is odd, the number of valid distributions is n // 2.
If n is even, n // 2 would give both sisters the same number,
so we subtract 1.

This can be simplified to (n - 1) // 2.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    print((n - 1) // 2)
