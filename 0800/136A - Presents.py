"""
Problem: 136A - Presents
Rating: 800
Link: https://codeforces.com/problemset/problem/136/A

Idea:
For each friend, store the friend who gave them a present. Since p[i] represents
the person who gave a gift to friend i+1, reverse this mapping by using a
dictionary. Then print the giver corresponding to each friend number from 1 to n.
"""

n=int(input())
p=list(map(int,input().split()))
d={}
for i in range(n):
    d[p[i]]=i+1
keys=list(d.keys())
keys.sort()
for i in keys:
    print(d[i],end=" ")
print()
