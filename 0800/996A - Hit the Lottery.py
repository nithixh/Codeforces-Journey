"""
Problem: 996A - Hit the Lottery
Rating: 800
Link: https://codeforces.com/problemset/problem/996/A

Idea:
To minimize the number of bills, always use the largest possible
denomination first.
For each denomination (100, 20, 10, 5, 1), take as many bills as
possible using integer division, then update the remaining amount
using the remainder.
The total number of bills used is the answer.
"""

n = int(input())
ans = 0
for bill in [100, 20, 10, 5, 1]:
    ans += n // bill
    n %= bill
print(ans)
