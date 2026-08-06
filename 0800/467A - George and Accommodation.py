"""
Problem: 467A - George and Accommodation
Rating: 800
Link: https://codeforces.com/problemset/problem/467/A

Idea:
For each room, calculate the number of free places by subtracting the current
occupancy from the room's capacity. If there are at least two free places,
George and Alex can move into that room. Count all such rooms.
"""

n=int(input())
ans=0
for i in range(n):
    p,q=map(int,input().split())
    if q-p>=2:
        ans+=1
print(ans)
