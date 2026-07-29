"""
Problem: 424A - Squats
Rating: 900
Link: https://codeforces.com/problemset/problem/424/A

Idea:
Count the number of standing ('X') and sitting ('x') hamsters. Identify the
position that appears fewer than n/2 times, then change the minimum number of
hamsters from the other position until both counts become equal. Output the
number of changes and one possible final arrangement.
"""

n=int(input())
s=input()
d={}
for i in s:
    d[i]=d.get(i,0)+1
mn=float('inf')
mc=''
for i in d:
    if d[i]<mn:
        mn=d[i]
        mc=i
rep = 'X' if mc=='x' else 'x'
if mn==n:
    mc,rep=rep,mc
    mn=0
c=n//2-mn
print(c)
sl=list(s)
for i in range(n):
    if c==0:
        break
    if sl[i]==rep:
        sl[i]=mc
        c-=1
print("".join(sl))
