"""
Problem: 412A - Poster
Rating: 900
Link: https://codeforces.com/problemset/problem/412/A

Idea:
We need to paint every character exactly once.

To minimize the total time, first move the ladder to the
nearest endpoint (position 1 or position n).

If the left endpoint is nearer:
    Move left until position 1.
    Print the first character.
    Keep moving right and printing the remaining characters.

Otherwise:
    Move right until position n.
    Print the last character.
    Keep moving left and printing the remaining characters.

This minimizes the initial movement, followed by exactly
n-1 movements between consecutive printing positions.
"""

n, k = map(int, input().split())
s = input()
ans = []
if k - 1 <= n - k:
    for _ in range(k - 1):
        ans.append("LEFT")
    ans.append("PRINT " + s[0])
    for i in range(1, n):
        ans.append("RIGHT")
        ans.append("PRINT " + s[i])
else:
    for _ in range(n - k):
        ans.append("RIGHT")
    ans.append("PRINT " + s[n - 1])
    for i in range(n - 2, -1, -1):
        ans.append("LEFT")
        ans.append("PRINT " + s[i])
print("\n".join(ans))
