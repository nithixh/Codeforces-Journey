"""
Problem: 549A - Face Detection
Rating: 900
Link: https://codeforces.com/problemset/problem/549/A

Idea:
Check every possible 2x2 square in the image. If its four characters can
form the word "face", count it as a face. Since the four characters can be
in any order, sort them and compare with the sorted version of "face".
"""

n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(input())
ans=0
for i in range(n-1):
    for j in range(m-1):
        s=a[i][j]+a[i][j+1]+a[i+1][j]+a[i+1][j+1]
        if sorted(s)==['a','c','e','f']:
            ans+=1
print(ans)
