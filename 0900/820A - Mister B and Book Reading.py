"""
Problem: 820A - Mister B and Book Reading
Rating: 900
Link: https://codeforces.com/problemset/problem/820/A

Idea:
On the first day, Mister B reads v0 pages.

From the second day onwards, his reading speed increases by a pages per day,
but it cannot exceed v1. Additionally, he has to reread l pages from the
previous day, so only (pages read today - l) pages are newly completed.

We simulate each day until the number of newly read pages reaches the total
number of pages c.

If the book can be finished on the first day, no rereading is needed.
"""

c, v0, v1, a, l = map(int, input().split())
remaining = c
remaining -= v0
if remaining <= 0:
    print(1)
else:
    days = 1
    speed = v0

    while remaining > 0:
        days += 1
        speed = min(speed + a, v1)
        remaining -= speed - l
    print(days)
