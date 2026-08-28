"""
Problem: 586A - Alena's Schedule
Rating: 900
Link: https://codeforces.com/problemset/problem/586/A

Idea:
Find the first and last pair that Alena has to attend. She stays at the
university between them, but if there are two or more consecutive empty
pairs, she can go home during that break. Therefore, count all pairs between
the first and last class, excluding empty pairs that belong to breaks of
length at least 2.
"""

n=int(input())
a=list(map(int,input().split()))
l=0
r=n-1
while l<n and a[l]==0:
    l+=1
while r>=0 and a[r]==0:
    r-=1
ans=0
i=l
while i<=r:
    if a[i]==1:
        ans+=1
        i+=1
    else:
        j=i
        while j<=r and a[j]==0:
            j+=1
        if j-i==1:
            ans+=1
        i=j
print(ans)
