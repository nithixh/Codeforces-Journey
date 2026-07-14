"""
Problem: 450A - Jzzhu and Children
Rating: 1000
Link: https://codeforces.com/problemset/problem/450/A

Idea:
Simulate the process using a queue. Each child is represented by their index and the
number of candies they still need. Repeatedly give the first child m candies. If they
still need more candies, move them to the end of the queue; otherwise, they leave.
When only one child remains in the queue, their index is the answer.
"""

from collections import deque
n,m=map(int,input().split())
need=list(map(int,input().split()))
dq=deque()
for i in range(n):
    dq.append([i+1,need[i]])
ans=1
while len(dq)>1:
    ind,candy=dq.popleft()
    candy=candy-m
    if candy>0:
        dq.append([ind,candy])
print(dq[0][0])
