"""
Problem: 2004B - Game with Doors
Rating: 1000
Link: https://codeforces.com/problemset/problem/2004/B

Idea:
Find the intersection of Alice's segment [l, r] and Bob's segment [L, R].

If the segments do not overlap, only one door between them needs to be
locked.

If they overlap, all doors inside the common part must be locked.
The number of such doors is:
    common_length - 1

Additionally, if the left endpoints are different, one extra door is
needed on the left side. Similarly, if the right endpoints are
different, one extra door is needed on the right side.

So:
answer = common_length - 1 + (l != L) + (r != R)
"""

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    common = min(r, R) - max(l, L) + 1
    if common <= 0:
        print(1)
    else:
        ans = common - 1
        ans += (l != L)
        ans += (r != R)
        print(ans)
