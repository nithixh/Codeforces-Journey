"""
Problem: 230A - Dragons
Rating: 1000
Link: https://codeforces.com/problemset/problem/230/A

Idea:
Sort all dragons by their strength in increasing order.

Kirito must have strictly greater strength than a dragon to defeat it.
After defeating a dragon, his strength increases by that dragon's bonus.

By fighting the weakest dragons first, Kirito gets the bonuses as early
as possible, making it possible to defeat stronger dragons later.

If Kirito cannot defeat any dragon in the sorted order, print "NO".
Otherwise, after defeating all dragons, print "YES".
"""

s,n=map(int,input().split())
dragons=[]
for i in range(n):
    x,y=map(int,input().split())
    dragons.append([x,y])
dragons.sort()
for x,y in dragons:
    if s>x:
        s+=y
    else:
        print("NO")
        break
else:
    print("YES")
