"""
Problem: 263A - Beautiful Matrix
Rating: 800
Link: https://codeforces.com/problemset/problem/263/A

Idea:
Find the position of '1' in the 5×5 matrix.
The minimum moves required is the Manhattan distance
from its current position to the center (2, 2).
"""

mat = []
x=0
y=0
for i in range(5):
    row=list(map(int,input().split()))
    mat.append(row)
    for j in range(5):
        if row[j]==1:
            x=i
            y=j
ans = abs(x-2)+abs(y-2)
print(ans)
