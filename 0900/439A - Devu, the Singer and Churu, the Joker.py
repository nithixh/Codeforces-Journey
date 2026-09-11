"""
Problem: 439A - Devu, the Singer and Churu, the Joker
Rating: 900
Link: https://codeforces.com/problemset/problem/439/A

Idea:
Devu needs sum(t) minutes to sing all n songs.

He also needs 10 minutes of rest after every song except the last one,
so the total required time is sum(t) + 10 * (n - 1).

If this time is greater than d, it is impossible.

Otherwise, the remaining time can be used by Churu for jokes.
Each joke takes 5 minutes, so the maximum number of jokes is
the remaining time divided by 5.
"""

n, d = map(int, input().split())
t = list(map(int, input().split()))
required = sum(t) + 10 * (n - 1)
if required > d:
    print(-1)
else:
    print((d - required) // 5)
