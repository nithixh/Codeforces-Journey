"""
Problem: 1362A - Johnny and Ancient Computer
Rating: 1000
Link: https://codeforces.com/problemset/problem/1362/A

Idea:
In each operation, we can multiply or divide a number by 2, 4, or 8.

First, remove all factors of 2 from both a and b.
If the remaining values are different, transforming a into b is
impossible, so print -1.

Otherwise, the larger number divided by the smaller number is a
power of 2. Count how many times we can divide this ratio by 8,
then handle any remaining factor of 2 or 4 in one operation.
"""

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    x = a
    y = b
    while x % 2 == 0:
        x //= 2
    while y % 2 == 0:
        y //= 2
    if x != y:
        print(-1)
        continue
    ratio = max(a, b) // min(a, b)
    ans = 0
    while ratio >= 8:
        ratio //= 8
        ans += 1
    if ratio > 1:
        ans += 1
    print(ans)
