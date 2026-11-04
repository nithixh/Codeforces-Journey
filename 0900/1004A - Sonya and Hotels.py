"""
Problem: 1004A - Sonya and Hotels
Rating: 900
Link: https://codeforces.com/problemset/problem/1004/A

Idea:
A new hotel must be at least distance d from every existing hotel.

There are always 2 possible positions:
- d units to the left of the first hotel.
- d units to the right of the last hotel.

For every pair of adjacent hotels:
- If the gap is exactly 2*d, only the middle position is possible.
- If the gap is greater than 2*d, two positions are possible:
  d units to the right of the left hotel and d units to the
  left of the right hotel.
- Otherwise, no position is possible.

Count all valid positions.
"""

n, d = map(int, input().split())
x = list(map(int, input().split()))

ans = 2

for i in range(n - 1):
    gap = x[i + 1] - x[i]

    if gap == 2 * d:
        ans += 1
    elif gap > 2 * d:
        ans += 2

print(ans)
