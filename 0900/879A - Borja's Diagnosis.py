"""
Problem: 879A - Borja's Diagnosis
Rating: 900
Link: https://codeforces.com/problemset/problem/879/A

Idea:
For each doctor, find the first day on which the doctor works that is
strictly after the day Borja visited the previous doctor.

Doctor i works on days s, s+d, s+2d, ...
So if the previous visit was on day cur, find the smallest value of this
sequence that is greater than cur. Keep updating cur for every doctor.
"""

n=int(input())
cur=0
for _ in range(n):
    s,d=map(int,input().split())
    if s>cur:
        cur=s
    else:
        k=(cur-s)//d+1
        cur=s+k*d
print(cur)
