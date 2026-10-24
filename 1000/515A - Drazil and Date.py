"""
Problem: 515A - Drazil and Date
Rating: 1000
Link: https://codeforces.com/problemset/problem/515/A

Idea:
The minimum number of steps needed to reach (a, b) from (0, 0) is
abs(a) + abs(b).

If s is smaller than this minimum, reaching the destination is impossible.

Otherwise, the extra steps must be even because Drazil can take
one step away and one step back, adding 2 steps without changing
his final position.

Therefore, print YES if s >= abs(a) + abs(b) and the difference
between them is even. Otherwise, print NO.
"""

a, b, s = map(int, input().split())
minimum = abs(a) + abs(b)
if s >= minimum and (s - minimum) % 2 == 0:
    print("Yes")
else:
    print("No")
