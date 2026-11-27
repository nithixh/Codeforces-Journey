"""
Problem: 1253A - Single Push
Rating: 1000
Link: https://codeforces.com/problemset/problem/1253/A

Idea:
Calculate the difference between corresponding elements:
    diff[i] = b[i] - a[i]

For a single push operation to work:
1. No difference can be negative.
2. All positive differences must have the same value k.
3. All positive differences must form one continuous segment.

If all differences are zero, the arrays are already equal.

Check these conditions and print YES or NO.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = [b[i] - a[i] for i in range(n)]
    if min(diff) < 0:
        print("NO")
        continue
    positive = [i for i in range(n) if diff[i] > 0]
    if not positive:
        print("YES")
        continue
    l = positive[0]
    r = positive[-1]
    k = diff[l]
    possible = True
    for i in range(l, r + 1):
        if diff[i] != k:
            possible = False
            break
    print("YES" if possible else "NO")
