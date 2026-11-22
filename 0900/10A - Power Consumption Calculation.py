"""
Problem: 10A - Power Consumption Calculation
Rating: 900
Link: https://codeforces.com/problemset/problem/10/A

Idea:
The laptop has 3 power consumption modes:
1. Normal mode: P1 watts per minute.
2. Screensaver mode: P2 watts per minute.
3. Sleep mode: P3 watts per minute.

During Tom's working intervals, the laptop always stays
in normal mode.

For every gap between two consecutive working intervals:
- First T1 minutes consume P1 per minute.
- Next T2 minutes consume P2 per minute.
- Remaining minutes consume P3 per minute.

Calculate the power consumed during all working intervals
and all gaps.
"""

n, p1, p2, p3, t1, t2 = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for l, r in intervals:
    ans += (r - l) * p1
for i in range(1, n):
    gap = intervals[i][0] - intervals[i - 1][1]
    first = min(gap, t1)
    ans += first * p1
    gap -= first
    second = min(gap, t2)
    ans += second * p2
    gap -= second
    ans += gap * p3
print(ans)
