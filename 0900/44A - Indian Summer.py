"""
Problem: 44A - Indian Summer
Rating: 900
Link: https://codeforces.com/problemset/problem/44/A

Idea:
Each leaf is uniquely identified by its combination of tree species and color.
We store every leaf description in a set, since a set automatically removes
duplicates. The number of unique descriptions is exactly the number of leaves
Alyona has picked.
"""

n=int(input())
leaves=[]
picked=set()
for i in range(n):
    leaves.append(input())
for i in leaves:
    picked.add(i)
print(len(picked))
