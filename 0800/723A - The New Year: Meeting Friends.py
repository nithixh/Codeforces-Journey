"""
Problem: 723A - The New Year: Meeting Friends
Rating: 800
Link: https://codeforces.com/problemset/problem/723/A

Idea:
The friends need to meet at one point. For three points on a line,
the optimal meeting point is the middle coordinate.

Our code calculates the total distance if they meet at each friend's
house and takes the minimum. This is equivalent to meeting at the
middle coordinate and gives the minimum total distance.
"""

x,y,z=map(int,input().split())
distxy=abs(x-y)
distxz=abs(x-z)
distyz=abs(y-z)
ans=[distxy+distxz,distxz+distyz,distxy+distyz]
print(min(ans))
