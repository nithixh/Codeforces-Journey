"""
Problem: 69A - Young Physicist
Rating: 1000
Link: http://codeforces.com/contest/69/problem/A

Idea:
If the sum of all x, y and z components is (0,0,0),
the body is in equilibrium.
"""
n=int(input())
x=y=z=0
for i in range(n):
    a,b,c=map(int,input().split())
    x+=a
    y+=b
    z+=c
if(x==y and y==z and x==0):
    print("YES")
else:
    print("NO")
