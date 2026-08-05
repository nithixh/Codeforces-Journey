"""
Problem: 677A - Vanya and Fence
Rating: 800
Link: https://codeforces.com/problemset/problem/677/A

Idea:
Each friend whose height is at most h occupies a width of 1, while each friend
taller than h bends down and occupies a width of 2. Sum the width contributed
by every friend to obtain the minimum required road width.
"""

n,h=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in a:
    if i>h:
        ans+=2
    else:
        ans+=1
print(ans)
