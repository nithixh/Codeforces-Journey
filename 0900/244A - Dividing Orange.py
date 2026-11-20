"""
Problem: 244A - Dividing Orange
Rating: 900
Link: https://codeforces.com/problemset/problem/244/A

Idea:
Each of the k children must receive exactly n segments.
Also, child i must receive their requested segment a[i].

First, assign the requested segment to each child.
Store these segments in separate lists.

Then, iterate through all segment numbers from 1 to n*k.
If a segment has not already been assigned, give it to
the next child who still needs more segments.

Finally, print the segments assigned to each child.
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = [[a[i]] for i in range(k)]
used = set(a)
child = 0
for x in range(1, n * k + 1):
    if x not in used:
        ans[child].append(x)
        if len(ans[child]) == n:
            child += 1
for group in ans:
    print(*group)
