"""
Problem: 263B - Squares
Rating: 900
Link: https://codeforces.com/problemset/problem/263/B

Idea:
If k is greater than the number of squares, it is impossible to have a point
belonging to exactly k squares.

Otherwise, sort the side lengths in descending order. Choosing the point
(a[k-1],a[k-1]) makes it belong to exactly the first k squares, since those
squares have side length at least a[k-1], while all remaining squares have
smaller side lengths.
"""

n,k=map(int,input().split())
a=list(map(int,input().split()))
if k>n:
    print(-1)
else:
    a.sort(reverse=True)
    print(a[k-1],a[k-1])
