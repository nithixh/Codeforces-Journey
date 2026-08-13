"""
Problem: 469A - I Wanna Be the Guy
Rating: 800
Link: https://codeforces.com/problemset/problem/469/A

Idea:
Store all the levels that can be passed by either Little X or Little Y in a
set. Since a set stores each level only once, if its size becomes n, all levels
can be passed by at least one of them. Otherwise, some levels are still missing.
"""

n=int(input())
plvl=list(map(int,input().split()))
qlvl=list(map(int,input().split()))
lvl=set()
for i in range(1,plvl[0]+1):
    lvl.add(plvl[i])
for i in range(1,qlvl[0]+1):
    lvl.add(qlvl[i])
if len(lvl)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
