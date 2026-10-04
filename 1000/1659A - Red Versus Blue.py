"""
Problem: 1659A - Red Versus Blue
Rating: 1000
Link: https://codeforces.com/problemset/problem/1659/A

Idea:
Place the b Blue wins as separators. This creates b + 1 groups of Red wins.

Distribute the r Red wins as evenly as possible among these groups.
This minimizes the maximum number of consecutive Red wins.

Each group gets r // (b + 1) Red wins, and the remaining
r % (b + 1) groups get one extra Red win.

Then place a B between every two groups.
"""

t = int(input())
for _ in range(t):
    n, r, b = map(int, input().split())
    groups = b + 1
    x = r // groups
    rem = r % groups
    ans = ""
    for i in range(groups):
        ans += "R" * (x + (1 if rem > 0 else 0))
        if rem > 0:
            rem -= 1
        if i < b:
            ans += "B"
    print(ans)
