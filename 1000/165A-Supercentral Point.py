"""
Problem: 165A - Supercentral Point
Rating: 1000
Link: https://codeforces.com/problemset/problem/165/A

Idea:
For every point, check whether there exists at least one point to its left, right,
above, and below. Since n ≤ 200, comparing every point with every other point
(O(n²)) is fast enough. If all four directions are found for a point, it is a
supercentral point.
"""

n=int(input())
points=[]
for _ in range(n):
    points.append(list(map(int,input().split())))
c=0
for i in range(n):
    x,y=points[i]
    ne=[0,0,0,0]
    for j in range(n):
        if i==j:
            continue
        x1,y1=points[j]
        if x1>x and y1==y:
            ne[0]+=1
        elif x1<x and y1==y:
            ne[1]+=1
        elif x1==x and y1>y:
            ne[2]+=1
        elif x1==x and y1<y:
            ne[3]+=1
        if all(ne):
            c+=1
            break
print(c)
