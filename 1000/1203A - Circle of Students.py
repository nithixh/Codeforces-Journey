"""
Problem: 1203A - Circle of Students
Rating: 1000
Link: https://codeforces.com/problemset/problem/1203/A

Idea:
Find the position of student 1 in the circle.

Starting from student 1, check whether the following students appear
in increasing order (2, 3, ..., n) when moving clockwise.

Also check whether they appear in increasing order when moving
counterclockwise.

If either direction works, print YES. Otherwise, print NO.
"""

q = int(input())
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    pos = p.index(1)
    clockwise = True
    counterclockwise = True
    for i in range(1, n):
        if p[(pos + i) % n] != i + 1:
            clockwise = False
        if p[(pos - i) % n] != i + 1:
            counterclockwise = False
    if clockwise or counterclockwise:
        print("YES")
    else:
        print("NO")
